#!/bin/bash

# valorile default pt flaguri
LIMITA_LINII=0
DATA_SINCE=""
DATA_FINAL=""
DATA_EXACTA=""

# functie pt usage (input format)
usage() {
    echo "Format: $0 [-n <numar_linii>] [-s <yyyy-mm-dd>] [-t <yyyy-mm-dd>] [-p <yyyy-mm-dd>] <path_la_file>"
    exit 1
}

# parseaza optiuni folosind getopts
while getopts ":n:s:t:p:" opt; do
    case $opt in
        n) LIMITA_LINII=$OPTARG ;;
        s) DATA_SINCE=$OPTARG ;;
        t) DATA_FINAL=$OPTARG ;;
        p) DATA_EXACTA=$OPTARG ;;
        *) usage ;;
    esac
done

# shifteaza optiunile parsate ca sa fie log fileul ultimul argument
shift $((OPTIND - 1))

# verifica daca este log file dat
if [[ $# -ne 1 ]]; then
    usage
fi

LOG_FILE=$1

# daca avem data pt -s transform in unix timestamp
if [[ -n $DATA_SINCE ]]; then
    DATA_SINCE_TS=$(date -d "$DATA_SINCE" +%s 2>/dev/null)
    if [[ $? -ne 0 ]]; then
        echo "Format invalid -s: $DATA_SINCE"
        exit 1
    fi
else
    DATA_SINCE_TS=0
fi

# daca avem data pt -t transform in unix timestamp (ts) iar
if [[ -n $DATA_FINAL ]]; then
    DATA_FINAL_TS=$(date -d "$DATA_FINAL" +%s 2>/dev/null)
    if [[ $? -ne 0 ]]; then
        echo "Format invalid -t: $DATA_FINAL"
        exit 1
    fi
else
    DATA_FINAL_TS=0
fi

# daca avem data pt -p data, verifica daca e valida
if [[ -n $DATA_EXACTA ]]; then
    DATA_EXACTA_VALID=$(date -d "$DATA_EXACTA" +%Y-%m-%d 2>/dev/null)
    if [[ $? -ne 0 ]]; then
        echo "Format invalid -p: $DATA_EXACTA"
        exit 1
    fi
else
    DATA_EXACTA_VALID=""
fi

# functie pt a procesa un log file
process_file() {
    local file=$1
    if [[ $file == *.gz ]]; then
        zgrep -a -E "session opened|session closed" "$file"
    else
        grep -a -E "session opened|session closed" "$file"
    fi
}

# functie pt a parsa si formata log lines
parse_log() {
    awk -v data_since_ts="$DATA_SINCE_TS" \
        -v data_final_ts="$DATA_FINAL_TS" \
        -v data_exacta="$DATA_EXACTA_VALID" '
        {
            split($1, datetime, "T")  # ptc is data si ora is despartite de T in log file
            log_date = datetime[1]    
            log_time_full = datetime[2]  # partea cu ora dar tot cu secunde si numere multe

            split(log_time_full, time_parts, "\\.")  # despartite de "."
            log_time = time_parts[1]  

            # convertul la unix timestamp pt comparatii
            cmd = "date -d \"" log_date "T" log_time "\" +%s"
            cmd | getline timestamp
            close(cmd)

            # aici is conditiile de afisare
            if (data_exacta != "") {
                if (log_date == data_exacta) {
                    if ($0 ~ /session opened/) {
                        printf "%-8s %-10s %-12s %s a fost deschis\n", log_time, log_date, $2, $3;
                    } else if ($0 ~ /session closed/) {
                        printf "%-8s %-10s %-12s %s a fost inchis\n", log_time, log_date, $2, $3;
                    }
                }
            } else if ((data_since_ts == 0 || timestamp >= data_since_ts) &&
                       (data_final_ts == 0 || timestamp <= data_final_ts)) {
                if ($0 ~ /session opened/) {
                    printf "%-8s %-10s %-12s %s a fost deschis\n", log_time, log_date, $2, $3;
                } else if ($0 ~ /session closed/) {
                    printf "%-8s %-10s %-12s %s a fost inchis\n", log_time, log_date, $2, $3;
                }
            }
        }
    '
}

# procesarea log file si afisarea cu line limit (optional)
if [[ $LIMITA_LINII -gt 0 ]]; then
    process_file "$LOG_FILE" | parse_log | head -n "$LIMITA_LINII"
else
    process_file "$LOG_FILE" | parse_log
fi

