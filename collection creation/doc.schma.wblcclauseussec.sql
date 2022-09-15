spool doc.schma.wblcclauseussec.out
--***************************************************************
--*  DOC.skel
--*
--*  Schema DDL for the Novus DOC Tables.  This will CREate
--*  - tables
--*  - indexes
--*  - constraints
--*  - grants
--*
--*  Optional content types:
--*  - The CONTENT table is optional and will be CREated if
--*    the "-f CTT" special flag is given to the CREshma script.
--*    The DDL is identified by  in the first column.
--*    content - what we mostly think of as text documents
--*
--*  - The MM_CONTENT table is optional and will be CREated if
--*    the "-f MMT" special flag is given to the CREshma script.
--*    The DDL is identified by ~MMT in the first column.
--*    mm_content - what we mostly think of as multimedia blobs: images, etc.
--*
--*  - The MM_FILE table is optional and will be CREated if
--*    the "-f MFT" special flag is given to the CREshma script.
--*    The DDL is identified by ~MFT in the first column.
--*    mm_file - streaming media too big to store directly in DOC.
--*    The table stores the guid, stage, and the location of where the mm is.
--*
--*  - The META_CONTENT table is optional and will be CREated if
--*    the "-f MCT" special flag is given to the CREshma script.
--*    The DDL is identified by  in the first column.
--* Meta_content?  Each of the 3 content types above can have metadata,
--*                additional content that describes the content. This
--*                metadata content is stored in the meta_content table.
--*                metadata content is stored in the meta_content table.
--*                You CAN'T have a guid with just metadata - the load will
--*                not allow this.  The guid must have one of the 3 content
--*                types associated with it, and in addition can have metadata.
--*                Therefore, DBA should never create a schema that just has
--*                a meta_content table.
--*
--*  - GSP04A1  - the database name
--*  - WBLCCLAUSEUSSEC - the schema name
--*  - -f options used in this run where
--*  - CTT - optional flag for CONTENT table
--*  - MCT - optional flag for META_CONTENT table
--*
--***************************************************************


create role docread;
create role docupd;
create user docr identified by n0vu5r default tablespace users;
create user docu identified by n0vu5u default tablespace users;
--# DMG 07/09/2015 add new generic novus users
create user novusr1 identified by n0vu5r default tablespace users;
create user novusr2 identified by n0vu5r default tablespace users;
create user devr identified by n0vu5r default tablespace users;
create user novusu1 identified by n0vu5u default tablespace users;
create user novusu2 identified by n0vu5u default tablespace users;
--# end DMG 07/09/2015
create user WBLCCLAUSEUSSEC identified by hnrtxpt default tablespace WBLCCLAUSEUSSECD;

grant connect to docread;
grant connect to docupd;
grant docread to docr;
grant docupd to docu;
--# DMG 07/09/2015 add new generic novus users
grant docread to novusr1;
grant docread to novusr2;
grant docread to devr;
grant docread to novusu1;
grant docread to novusu2;
grant docupd to novusu1;
grant docupd to novusu2;
--# end DMG 07/09/2015
grant connect,resource to WBLCCLAUSEUSSEC;
alter user WBLCCLAUSEUSSEC quota unlimited on WBLCCLAUSEUSSECD;

CREATE TABLE WBLCCLAUSEUSSEC.COMPRESSION (COMPRESSION_CODE NUMBER(6) NOT NULL,
COMPRESSION_DESC VARCHAR2(20 byte) NOT NULL,
CONSTRAINT WBLCCLAUSEUSSEC_XPKCOMP UNIQUE(COMPRESSION_CODE)
USING INDEX
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10)
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10
LOGGING;

INSERT INTO WBLCCLAUSEUSSEC.COMPRESSION VALUES (0,'uncompressed');
INSERT INTO WBLCCLAUSEUSSEC.COMPRESSION VALUES (1,'zlib compressed');
INSERT INTO WBLCCLAUSEUSSEC.COMPRESSION VALUES (2,'encrypted');
INSERT INTO WBLCCLAUSEUSSEC.COMPRESSION VALUES (3,'compbeforeencrypt');


CREATE TABLE WBLCCLAUSEUSSEC.CONTENT (GUID VARCHAR2(33 byte) NOT NULL,
STAGE_NUM NUMBER(11) DEFAULT 0 NOT NULL,
BODY BLOB,
BODY_FULL_BC NUMBER(11) DEFAULT 0 NOT NULL,
BODY_COMP_BC NUMBER(11) DEFAULT 0 NOT NULL,
BODY_COMP_CODE NUMBER(6) DEFAULT 0 NOT NULL,
STRUCT BLOB,
STRUCT_COMP_BC NUMBER(11) DEFAULT 0 NOT NULL,
STRUCT_COMP_CODE NUMBER(6) DEFAULT 0 NOT NULL,
DIR_FULL_BC NUMBER(11) DEFAULT 0 NOT NULL,
WORDPOS_FULL_BC NUMBER(11) DEFAULT 0,
DEL_FLAG CHAR(1 byte) DEFAULT 'N' NOT NULL,
INCLUDE_CODE CHAR(1 byte),
RELOAD_ID NUMBER(11),
CHUNK_COUNT NUMBER(11),
WORD_POS_MAP BLOB,
WORD_POS_COMP_BC NUMBER(11),
WORD_POS_COMP_CODE NUMBER(6),
CHUNK_INFO BLOB,
CHUNK_INFO_FULL_BC NUMBER(11),
CHUNK_INFO_COMP_BC NUMBER(11),
CHUNK_INFO_COMP_CODE NUMBER(6),
CHUNK_COMP_OFFSETS BLOB,
CHUNK_COMP_OFF_LEN NUMBER(11),
CONSTRAINT WBLCCLAUSEUSSEC_BCCC FOREIGN KEY(BODY_COMP_CODE)
REFERENCES WBLCCLAUSEUSSEC.COMPRESSION(COMPRESSION_CODE),
CONSTRAINT WBLCCLAUSEUSSEC_CDFC CHECK(DEL_FLAG IN ('Y','N')),
CONSTRAINT WBLCCLAUSEUSSEC_SCCC FOREIGN KEY(STRUCT_COMP_CODE)
REFERENCES WBLCCLAUSEUSSEC.COMPRESSION(COMPRESSION_CODE),
CONSTRAINT WBLCCLAUSEUSSEC_XPKC UNIQUE(GUID, STAGE_NUM, DEL_FLAG)
USING INDEX
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10)
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10
LOGGING
LOB(BODY) STORE AS  CONTENT_BODY_D ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0 )
LOB(STRUCT) STORE AS  CONTENT_STRUCT_D ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0 )
LOB(WORD_POS_MAP) STORE AS  ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0 )
LOB(CHUNK_INFO) STORE AS  ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0 )
LOB(CHUNK_COMP_OFFSETS) STORE AS  ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0 );

create index WBLCCLAUSEUSSEC.RELOAD_CTT_IX on WBLCCLAUSEUSSEC.CONTENT(RELOAD_ID) tablespace WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10;

CREATE TABLE WBLCCLAUSEUSSEC.WPOS (GUID VARCHAR2(33) NOT NULL,
COLLECTION_ID NUMBER(11,0) NOT NULL,
STAGE_NUM NUMBER(11,0) NOT NULL,
DEL_FLAG CHAR(1) NOT NULL,
WORD_POS_MAP BLOB,
WORDPOS_FULL_BC NUMBER(11,0),
WORD_POS_COMP_BC NUMBER(11,0),
WORD_POS_COMP_CODE NUMBER(6),
RELOAD_ID NUMBER(11,0),
CONSTRAINT WBLCCLAUSEUSSEC_PK_WPOS PRIMARY KEY (GUID, COLLECTION_ID, STAGE_NUM, DEL_FLAG)
USING INDEX
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10)
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10
LOGGING
LOB(WORD_POS_MAP) STORE AS  ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0 );

CREATE TABLE WBLCCLAUSEUSSEC.META_CONTENT (GUID VARCHAR2(33 byte) NOT NULL,
STAGE_NUM NUMBER(11) DEFAULT 0 NOT NULL,
BODY BLOB,
BODY_FULL_BC NUMBER(11) DEFAULT 0 NOT NULL,
BODY_COMP_BC NUMBER(11) DEFAULT 0 NOT NULL,
BODY_COMP_CODE NUMBER(6) DEFAULT 0 NOT NULL,
STRUCT BLOB,
STRUCT_COMP_BC NUMBER(11) DEFAULT 0 NOT NULL,
STRUCT_COMP_CODE NUMBER(6) DEFAULT 0 NOT NULL,
DIR_FULL_BC NUMBER(11) DEFAULT 0 NOT NULL,
DEL_FLAG CHAR(1 byte) DEFAULT 'N' NOT NULL,
RELOAD_ID NUMBER(11), 
CONSTRAINT WBLCCLAUSEUSSEC_BCCMC FOREIGN KEY(BODY_COMP_CODE)
REFERENCES WBLCCLAUSEUSSEC.COMPRESSION(COMPRESSION_CODE),
CONSTRAINT WBLCCLAUSEUSSEC_CDFMC CHECK(DEL_FLAG IN ('Y','N')),
CONSTRAINT WBLCCLAUSEUSSEC_SCCMC FOREIGN KEY(STRUCT_COMP_CODE)
REFERENCES WBLCCLAUSEUSSEC.COMPRESSION(COMPRESSION_CODE),
CONSTRAINT WBLCCLAUSEUSSEC_XPKMC UNIQUE(GUID, STAGE_NUM, DEL_FLAG)
USING INDEX
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10)
TABLESPACE WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10
LOGGING
LOB(BODY) STORE AS  META_CONTENT_BODY_D ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0 )
LOB(STRUCT) STORE AS  META_CONTENT_STRUCT_D ( TABLESPACE WBLCCLAUSEUSSECD ENABLE STORAGE IN ROW CACHE  FREEPOOLS 1 CHUNK 8192 PCTVERSION 0);

create index WBLCCLAUSEUSSEC.RELOAD_MCT_IX on WBLCCLAUSEUSSEC.META_CONTENT(RELOAD_ID) tablespace WBLCCLAUSEUSSECD PCTFREE 10 INITRANS 10;


grant select,insert,update,delete on WBLCCLAUSEUSSEC.compression to docupd;
grant select,insert,update,delete on WBLCCLAUSEUSSEC.content to docupd;
grant select,insert,update,delete on WBLCCLAUSEUSSEC.wpos to docupd;
grant select,insert,update,delete on WBLCCLAUSEUSSEC.meta_content to docupd;
grant select on WBLCCLAUSEUSSEC.compression to docread;
grant select on WBLCCLAUSEUSSEC.content to docread;
grant select on WBLCCLAUSEUSSEC.wpos to docread;
grant select on WBLCCLAUSEUSSEC.meta_content to docread;

spool off
