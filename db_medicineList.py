import mariadb
import sys

import db_conn

def get_medicine_list_name(medicineName):
    global medicineSeq, entpSeq, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode
    global result_list, result_count

    result_list = []
    result_count = 0

    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_query = "select medicineSeq, medicineName, entpSeq, entpName, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode " \
                   "from medicineList " \
                   "where medicineName like ? or medicineEngName like ?"

    # print(select_query)

    cur.execute(select_query, (("%"+medicineName+"%"), ("%"+medicineName+"%")))
    # print(cur)
    result_set = cur.fetchall()

    for result_medicineSeq, result_medicineName, result_entpSeq, result_entpName, result_chart, result_medicineImage, result_printFront, result_printBack, result_medicineShape, result_colorClass1, result_colorClass2, result_lineFront, result_lineBack, result_lengLong, result_lengShort, result_thick, result_imgRegistTs, result_classNo, result_className, result_etcOtcName, result_medicinePermitDate, result_formCodeName, result_markCodeFrontAnal, result_markCodeBackAnal, result_markCodeFrontImg, result_markCodeBackImg, result_changeDate, result_markCodeFront, result_markCodeBack, result_medicineEngName, result_ediCode in result_set:
        # medicineSeq = result_medicineSeq
        # medicineName = result_medicineName
        # entpSeq = result_entpSeq
        # chart = result_chart
        # medicineImage = result_medicineImage
        # printFront = result_printFront
        # printBack = result_printBack
        # medicineShape = result_medicineShape
        # colorClass1 = result_colorClass1
        # colorClass2 = result_colorClass2
        # lineFront = result_lineFront
        # lineBack = result_lineBack
        # lengLong = result_lengLong
        # lengShort = result_lengShort
        # thick = result_thick
        # imgRegistTs = result_imgRegistTs
        # classNo = result_classNo
        # className = result_className
        # etcOtcName = result_etcOtcName
        # medicinePermitDate = result_medicinePermitDate
        # formCodeName = result_formCodeName
        # markCodeFrontAnal = result_markCodeFrontAnal
        # markCodeBackAnal = result_markCodeBackAnal
        # markCodeFrontImg = result_markCodeFrontImg
        # markCodeBackImg = result_markCodeBackImg
        # changeDate = result_changeDate
        # markCodeFront = result_markCodeFront
        # markCodeBack = result_markCodeBack
        # medicineEngName = result_medicineEngName
        # ediCode = result_ediCode
        result_list.append({"medicineSeq": result_medicineSeq,
            "medicineName": result_medicineName,
            "entpSeq": result_entpSeq,
            "entpName": result_entpName,
            "chart": result_chart,
            "medicineImage": result_medicineImage,
            "printFront": result_printFront,
            "printBack": result_printBack,
            "medicineShape": result_medicineShape,
            "colorClass1": result_colorClass1,
            "colorClass2": result_colorClass2,
            "lineFront": result_lineFront,
            "lineBack": result_lineBack,
            "lengLong": result_lengLong,
            "lengShort": result_lengShort,
            "thick": result_thick,
            "imgRegistTs": result_imgRegistTs,
            "classNo": result_classNo,
            "className": result_className,
            "etcOtcName": result_etcOtcName,
            "medicinePermitDate": result_medicinePermitDate,
            "formCodeName": result_formCodeName,
            "markCodeFrontAnal": result_markCodeFrontAnal,
            "markCodeBackAnal": result_markCodeBackAnal,
            "markCodeFrontImg": result_markCodeFrontImg,
            "markCodeBackImg": result_markCodeBackImg,
            "changeDate": result_changeDate,
            "markCodeFront": result_markCodeFront,
            "markCodeBack": result_markCodeBack,
            "medicineEngName": result_medicineEngName,
            "ediCode": result_ediCode})
        result_count+=1

    # print(result_list)
    # print(result_count)
    return {"resultCount": result_count,
            "medicineItem": result_list}

def get_medicine_list_shape(shape, medicineColor, medicineLine, medicineCode):
    global medicineSeq, entpSeq, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode
    global result_list, result_count

    result_list = []
    result_count = 0

    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_query = "select medicineSeq, medicineName, entpSeq, entpName, chart, medicineImage, printFront, printBack, medicineShape, colorClass1, colorClass2, lineFront, lineBack, lengLong, lengShort, thick, imgRegistTs, classNo, className, etcOtcName, medicinePermitDate, formCodeName, markCodeFrontAnal, markCodeBackAnal, markCodeFrontImg, markCodeBackImg, changeDate, markCodeFront, markCodeBack, medicineEngName, ediCode " \
                   "from medicineList " \
                   "where medicineShape like ? and " \
                   "colorClass1 like ? or colorClass2 like ? and " \
                   "lineFront like ? or lineBack like ? and " \
                   "printFront like ? or printBack like ? " \
                   "Limit 30"
    # print(select_query)
    cur.execute(select_query, (("%"+shape+"%"),
                               ("%"+medicineColor+"%"), ("%"+medicineColor+"%"),
                               ("%"+medicineLine+"%"), ("%"+medicineLine+"%"),
                               ("%"+medicineCode+"%"), ("%"+medicineCode+"%")))
    result_set = cur.fetchall()

    for result_medicineSeq, result_medicineName, result_entpSeq, result_entpName, result_chart, result_medicineImage, result_printFront, result_printBack, result_medicineShape, result_colorClass1, result_colorClass2, result_lineFront, result_lineBack, result_lengLong, result_lengShort, result_thick, result_imgRegistTs, result_classNo, result_className, result_etcOtcName, result_medicinePermitDate, result_formCodeName, result_markCodeFrontAnal, result_markCodeBackAnal, result_markCodeFrontImg, result_markCodeBackImg, result_changeDate, result_markCodeFront, result_markCodeBack, result_medicineEngName, result_ediCode in result_set:
        # medicineSeq = result_medicineSeq
        # medicineName = result_medicineName
        # entpSeq = result_entpSeq
        # chart = result_chart
        # medicineImage = result_medicineImage
        # printFront = result_printFront
        # printBack = result_printBack
        # medicineShape = result_medicineShape
        # colorClass1 = result_colorClass1
        # colorClass2 = result_colorClass2
        # lineFront = result_lineFront
        # lineBack = result_lineBack
        # lengLong = result_lengLong
        # lengShort = result_lengShort
        # thick = result_thick
        # imgRegistTs = result_imgRegistTs
        # classNo = result_classNo
        # className = result_className
        # etcOtcName = result_etcOtcName
        # medicinePermitDate = result_medicinePermitDate
        # formCodeName = result_formCodeName
        # markCodeFrontAnal = result_markCodeFrontAnal
        # markCodeBackAnal = result_markCodeBackAnal
        # markCodeFrontImg = result_markCodeFrontImg
        # markCodeBackImg = result_markCodeBackImg
        # changeDate = result_changeDate
        # markCodeFront = result_markCodeFront
        # markCodeBack = result_markCodeBack
        # medicineEngName = result_medicineEngName
        # ediCode = result_ediCode
        result_list.append({"medicineSeq": result_medicineSeq,
                            "medicineName": result_medicineName,
                            "entpSeq": result_entpSeq,
                            "entpName": result_entpName,
                            "chart": result_chart,
                            "medicineImage": result_medicineImage,
                            "printFront": result_printFront,
                            "printBack": result_printBack,
                            "medicineShape": result_medicineShape,
                            "colorClass1": result_colorClass1,
                            "colorClass2": result_colorClass2,
                            "lineFront": result_lineFront,
                            "lineBack": result_lineBack,
                            "lengLong": result_lengLong,
                            "lengShort": result_lengShort,
                            "thick": result_thick,
                            "imgRegistTs": result_imgRegistTs,
                            "classNo": result_classNo,
                            "className": result_className,
                            "etcOtcName": result_etcOtcName,
                            "medicinePermitDate": result_medicinePermitDate,
                            "formCodeName": result_formCodeName,
                            "markCodeFrontAnal": result_markCodeFrontAnal,
                            "markCodeBackAnal": result_markCodeBackAnal,
                            "markCodeFrontImg": result_markCodeFrontImg,
                            "markCodeBackImg": result_markCodeBackImg,
                            "changeDate": result_changeDate,
                            "markCodeFront": result_markCodeFront,
                            "markCodeBack": result_markCodeBack,
                            "medicineEngName": result_medicineEngName,
                            "ediCode": result_ediCode})
        result_count += 1

    # print(result_list)
    # print(result_count)
    return {"resultCount": result_count,
            "medicineItem": result_list}