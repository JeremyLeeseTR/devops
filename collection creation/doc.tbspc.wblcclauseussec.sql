spool doc.tbspc.wblcclauseussec.out
-- This DDL file is used to generate the scripts to create a Novus Oracle DOC tablespaces.
--
CREATE TABLESPACE WBLCCLAUSEUSSECD
LOGGING
extent management local autoallocate
segment space management auto
  DATAFILE  '/s01/oradata1/gsp04/gsp04_doc_wblcclauseussec_d01.dbf' SIZE 600M
autoextend off blocksize 8192;
spool off
