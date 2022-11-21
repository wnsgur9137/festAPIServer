import mariadb
import sys

import db_conn

def get_medicineInfo_list(medicineName):
    global drugSeq, drugName, entpName, efcyQesitm, useMethodQesitm, atpnWarnQesitm, atpnQesitm, intrcQesitm, seQesitm, depositMethodQesitm, openDe, updateDe, drugImage
    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_query = "select drugSeq, drugName, entpName, efcyQesitm, useMethodQesitm, atpnWarnQesitm, atpnQesitm, intrcQesitm, seQesitm, depositMethodQesitm, openDe, updateDe, drugImage " \
                   "from easyDrugList " \
                   "where drugName=?"

    cur.execute(select_query, (medicineName,))
    result_set = cur.fetchall()

    for result_drugSeq, result_drugName, result_entpName, result_efcyQesitm, result_useMethodQesitm, result_atpnWarnQesitm, result_atpnQesitm, result_intrcQesitm, result_seQesitm, result_depositMethodQesitm, result_openDe, result_updateDe, result_drugImage in result_set:
        drugSeq = result_drugSeq
        drugName = result_drugName
        entpName = result_entpName
        efcyQesitm = result_efcyQesitm
        useMethodQesitm = result_useMethodQesitm
        atpnWarnQesitm = result_atpnWarnQesitm
        atpnQesitm = result_atpnQesitm
        intrcQesitm = result_intrcQesitm
        seQesitm = result_seQesitm
        depositMethodQesitm = result_depositMethodQesitm
        openDe = result_openDe
        updateDe = result_updateDe
        drugImage = result_drugImage

    return {"drugSeq": drugSeq,
            "drugName": drugName,
            "entpName": entpName,
            "efcyQesitm": efcyQesitm,
            "useMethodQesitm": useMethodQesitm,
            "atpnWarnQesitm": atpnWarnQesitm,
            "atpnQesitm": atpnQesitm,
            "intrcQesitm": intrcQesitm,
            "seQesitm": seQesitm,
            "depositMethodQesitm": depositMethodQesitm,
            "openDe": openDe,
            "updateDe": updateDe,
            "drugImage": drugImage}
