import mariadb
import sys

import db_conn

def get_medicine_list_name(medicineName):
    global medicineSeq, entpSeq, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode
    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_query = "select medicineSeq, medicineName, entpSeq, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode " \
                   "from medicineList " \
                   "where medicineName like ? or medicineEngName like ?"

    print(select_query)

    cur.execute(select_query, (("%"+medicineName+"%"), ("%"+medicineName+"%")))
    print(cur)
    result_set = cur.fetchall()

    for result_medicineSeq, result_medicineName, result_entpSeq, result_chart, result_medicineImage, result_printFront, result_printBack, result_medicineShape, result_colorClass1, result_colorClass2, result_lineFront, result_lineBack, result_lengLong, result_lengShort, result_thick, result_imgRegistTs, result_classNo, result_className, result_etcOtcName, result_medicinePermitDate, result_formCodeName, result_markCodeFrontAnal, result_markCodeBackAnal, result_markCodeFrontImg, result_markCodeBackImg, result_changeDate, result_markCodeFront, result_markCodeBack, result_medicineEngName, result_ediCode in result_set:
        medicineSeq = result_medicineSeq
        medicineName = result_medicineName
        entpSeq = result_entpSeq
        chart = result_chart
        medicineImage = result_medicineImage
        printFront = result_printFront
        printBack = result_printBack
        medicineShape = result_medicineShape
        colorClass1 = result_colorClass1
        colorClass2 = result_colorClass2
        lineFront = result_lineFront
        lineBack = result_lineBack
        lengLong = result_lengLong
        lengShort = result_lengShort
        thick = result_thick
        imgRegistTs = result_imgRegistTs
        classNo = result_classNo
        className = result_className
        etcOtcName = result_etcOtcName
        medicinePermitDate = result_medicinePermitDate
        formCodeName = result_formCodeName
        markCodeFrontAnal = result_markCodeFrontAnal
        markCodeBackAnal = result_markCodeBackAnal
        markCodeFrontImg = result_markCodeFrontImg
        markCodeBackImg = result_markCodeBackImg
        changeDate = result_changeDate
        markCodeFront = result_markCodeFront
        markCodeBack = result_markCodeBack
        medicineEngName = result_medicineEngName
        ediCode = result_ediCode

    return {"medicineSeq": medicineSeq,
            "medicineName": medicineName,
            "entpSeq": entpSeq,
            "chart": chart,
            "medicineImage": medicineImage,
            "printFront": printFront,
            "printBack": printBack,
            "medicineShape": medicineShape,
            "colorClass1": colorClass1,
            "colorClass2": colorClass2,
            "lineFront": lineFront,
            "lineBack": lineBack,
            "lengLong": lengLong,
            "lengShort": lengShort,
            "thick": thick,
            "imgRegistTs": imgRegistTs,
            "classNo": classNo,
            "className": className,
            "etcOtcName": etcOtcName,
            "medicinePermitDate": medicinePermitDate,
            "formCodeName": formCodeName,
            "markCodeFrontAnal": markCodeFrontAnal,
            "markCodeBackAnal": markCodeBackAnal,
            "markCodeFrontImg": markCodeFrontImg,
            "markCodeBackImg": markCodeBackImg,
            "changeDate": changeDate,
            "markCodeFront": markCodeFront,
            "markCodeBack": markCodeBack,
            "medicineEngName": medicineEngName,
            "ediCode": ediCode}

def get_medicine_list_shape(medicineName):
    global medicineSeq, entpSeq, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode
    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_query = "select medicineSeq, medicineName, entpSeq, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode " \
                   "from medicineList " \
                   "where medicineName = ? or medicineEngName = ?"

    cur.execute(select_query, (("%"+medicineName+"%"), ("%"+medicineName+"%")))
    result_set = cur.fetchall()

    for result_medicineSeq, result_medicineName, result_entpSeq, result_chart, result_medicineImage, result_printFront, result_printBack, result_medicineShape, result_colorClass1, result_colorClass2, result_lineFront, result_lineBack, result_lengLong, result_lengShort, result_thick, result_imgRegistTs, result_classNo, result_className, result_etcOtcName, result_medicinePermitDate, result_formCodeName, result_markCodeFrontAnal, result_markCodeBackAnal, result_markCodeFrontImg, result_markCodeBackImg, result_changeDate, result_markCodeFront, result_markCodeBack, result_medicineEngName, result_ediCode in result_set:
        medicineSeq = result_medicineSeq
        medicineName = result_medicineName
        entpSeq = result_entpSeq
        chart = result_chart
        medicineImage = result_medicineImage
        printFront = result_printFront
        printBack = result_printBack
        medicineShape = result_medicineShape
        colorClass1 = result_colorClass1
        colorClass2 = result_colorClass2
        lineFront = result_lineFront
        lineBack = result_lineBack
        lengLong = result_lengLong
        lengShort = result_lengShort
        thick = result_thick
        imgRegistTs = result_imgRegistTs
        classNo = result_classNo
        className = result_className
        etcOtcName = result_etcOtcName
        medicinePermitDate = result_medicinePermitDate
        formCodeName = result_formCodeName
        markCodeFrontAnal = result_markCodeFrontAnal
        markCodeBackAnal = result_markCodeBackAnal
        markCodeFrontImg = result_markCodeFrontImg
        markCodeBackImg = result_markCodeBackImg
        changeDate = result_changeDate
        markCodeFront = result_markCodeFront
        markCodeBack = result_markCodeBack
        medicineEngName = result_medicineEngName
        ediCode = result_ediCode

    return {"medicineSeq": medicineSeq,
            "medicineName": medicineName,
            "entpSeq": entpSeq,
            "chart": chart,
            "medicineImage": medicineImage,
            "printFront": printFront,
            "printBack": printBack,
            "medicineShape": medicineShape,
            "colorClass1": colorClass1,
            "colorClass2": colorClass2,
            "lineFront": lineFront,
            "lineBack": lineBack,
            "lengLong": lengLong,
            "lengShort": lengShort,
            "thick": thick,
            "imgRegistTs": imgRegistTs,
            "classNo": classNo,
            "className": className,
            "etcOtcName": etcOtcName,
            "medicinePermitDate": medicinePermitDate,
            "formCodeName": formCodeName,
            "markCodeFrontAnal": markCodeFrontAnal,
            "markCodeBackAnal": markCodeBackAnal,
            "markCodeFrontImg": markCodeFrontImg,
            "markCodeBackImg": markCodeBackImg,
            "changeDate": changeDate,
            "markCodeFront": markCodeFront,
            "markCodeBack": markCodeBack,
            "medicineEngName": medicineEngName,
            "ediCode": ediCode}