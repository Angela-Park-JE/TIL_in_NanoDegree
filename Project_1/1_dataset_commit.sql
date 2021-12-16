-- 현재: 유저명을 OLITE_ADMIN 으로 생성 후 변경하는 SQL문 작성해야 함. 변경방법을 찾지 못함



-- 1. USER 만들기 및 권한 부여 (pdb_system 에서 생성)
CREATE USER OLITE_ADMIN IDENTIFIED BY password;

GRANT DBA TO OLITE_ADMIN;

GRANT CREATE SESSION TO OLITE_ADMIN;

GRANT CREATE TABLE TO OLITE_ADMIN;



-- 2. 접속 탭에서 테이블 우클릭 - 팝업 창에서 데이터셋 선택
-- 3. 임포트 방식에서 SQL LOADER UTILITY 선택
-- 4. 대상 테이블 각 컬럼명, 데이터타입, 자릿수, 설명 등 입력
-- 5. 완료에서 생성된 파일 디렉토리의 저장위치만 따로 지정함(기존 데이터셋 내 폴더 생성함)
-- 6. 팝업창이 꺼지면서 COMMIT 되었다고 뜰 때 데이터가 다 들어간 것이 아니라 테이블만 생성 된 것임 
----  테이블을 만드는 쿼리가 작성되고, F5로 실행하면 된다.
-- 7. 이때 테이블이 만들어지면 테이블 내 해당 테이블을 우클릭 하고 데이터 임포트 과정을 한 번 더 실행하면 로우를 넣고있다는 과정 창이 뜨게 됨

-- 8-1. 데이터 입력까지 완료 후 데이터 확인하는 쿼리
SELECT *
FROM orders
WHERE ROWNUM<10;

-- 8-2. 전체 로우 개수 확인하는 쿼리
SELECT COUNT(*) AS COUNTS
FROM orders;
-- 결과: 99441로 COUNTS라는 컬럼아래 뜬다. 실제 데이터 셋과 일치함을 확인했다.
