-- 학생 ------------------------------------------------------------------------

-- 또래지명----------------------------------------------------------------------
SELECT 
	CAST(AES_DECRYPT( UNHEX(C.STUDENT_NAME), 'ehfhtl2015') AS CHAR) AS '지명한 학생',
	C.STUDENT_NUM '학번',
	CASE WHEN C.STUDENT_SEX = 1 THEN '남' ELSE '여' END  '성별',
	B.QUESTION_NO '문항번호',
	CAST(AES_DECRYPT( UNHEX(D.STUDENT_NAME), 'ehfhtl2015') AS CHAR) AS '지명받은 학생'
FROM psy_target_detail A, at_user_testing_paper_pn B, school_student C, school_student D
WHERE 
	A.USER_TESTING_NO = B.USER_TESTING_NO
	AND A.TARGET_CODE = C.STUDENT_CODE
	AND B.STUDENT_CODE = D.STUDENT_CODE
	AND A.PSY_CODE = 'P2025052995C9'
	AND A.CLASS_CODE = 'AC000120253047CE9'
	AND A.PSY_TARGET = 'STUDENT';	
-- 또래지명----------------------------------------------------------------------

-- 자기보고----------------------------------------------------------------------
SELECT 
	CAST(AES_DECRYPT( UNHEX(C.STUDENT_NAME), 'ehfhtl2015') AS CHAR) AS STUDENT_NAME,
	C.STUDENT_NUM '학번',
	CASE WHEN C.STUDENT_SEX = 1 THEN '남' ELSE '여' END  '성별',
	B.PAPER_JSON '응답값'
FROM psy_target_detail A, at_user_testing_paper B, school_student C
WHERE 
	A.USER_TESTING_NO = B.USER_TESTING_NO
	AND A.TARGET_CODE = C.STUDENT_CODE
	AND A.PSY_CODE = 'P2025052995C9'
	AND A.CLASS_CODE = 'AC000120253047CE9'
	AND A.PSY_TARGET = 'STUDENT';
-- 자기보고----------------------------------------------------------------------	

-- 문장완성----------------------------------------------------------------------	
SELECT 
	CAST(AES_DECRYPT( UNHEX(C.STUDENT_NAME), 'ehfhtl2015') AS CHAR) AS '학생명',
	C.STUDENT_NUM '학번',
	CASE WHEN C.STUDENT_SEX = 1 THEN '남' ELSE '여' END  '성별',
	B.QUESTION_NO '문항번호',
	B.INPUT_DATA '응답값'
FROM psy_target_detail A, at_user_testing_paper_sct B, school_student C
WHERE 
	A.USER_TESTING_NO = B.USER_TESTING_NO
	AND A.TARGET_CODE = C.STUDENT_CODE
	AND A.PSY_CODE = 'P2025052995C9'
	AND A.CLASS_CODE = 'AC000120253047CE9'
	AND A.PSY_TARGET = 'STUDENT';
-- 문장완성----------------------------------------------------------------------	

-- 학생 ------------------------------------------------------------------------

-- 선생 ------------------------------------------------------------------------
-- 학생평가----------------------------------------------------------------------	
SELECT  
	CAST(AES_DECRYPT(UNHEX(C.STUDENT_NAME), 'ehfhtl2015') AS CHAR) AS '학생명',
	B.QUESTION_NO AS '문항번호',
	B.SELECT_DATA AS '응답값'
FROM psy_target_detail A, at_user_testing_paper_tr B, school_student C
WHERE 
	A.USER_TESTING_NO = B.USER_TESTING_NO
	AND B.STUDENT_CODE = C.STUDENT_CODE
	AND A.PSY_CODE = 'P2025052995C9'
	AND A.CLASS_CODE = 'AC000120253047CE9'
	AND A.PSY_TARGET = 'TEACHER';		
-- 학생평가----------------------------------------------------------------------	

-- 자기보고----------------------------------------------------------------------	
SELECT 
	B.PAPER_JSON '응답값'
FROM psy_target_detail A, at_user_testing_paper B
WHERE 
	A.USER_TESTING_NO = B.USER_TESTING_NO
	AND A.PSY_CODE = 'P2025052995C9'
	AND A.CLASS_CODE = 'AC000120253047CE9'
	AND A.PSY_TARGET = 'TEACHER';	
-- 자기보고----------------------------------------------------------------------	

-- 선생 ------------------------------------------------------------------------