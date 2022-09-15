-- DROP SCHEMA newcollection;

CREATE SCHEMA newcollection AUTHORIZATION postgres;

-- DROP TYPE newcollection.compression;

/*
CREATE TYPE newcollection.compression AS (
	compression_code numeric(6,0),
	compression_desc varchar(20));

-- DROP TYPE newcollection."content";

CREATE TYPE newcollection."content" AS (
	guid varchar(33),
	stage_num numeric(11,0),
	body bytea,
	body_full_bc numeric(11,0),
	body_comp_bc numeric(11,0),
	body_comp_code numeric(6,0),
	struct bytea,
	struct_comp_bc numeric(11,0),
	struct_comp_code numeric(6,0),
	dir_full_bc numeric(11,0),
	wordpos_full_bc numeric(11,0),
	del_flag bpchar(1),
	include_code bpchar(1),
	reload_id numeric(11,0),
	chunk_count numeric(11,0),
	word_pos_map bytea,
	word_pos_comp_bc numeric(11,0),
	word_pos_comp_code numeric(6,0),
	chunk_info bytea,
	chunk_info_full_bc numeric(11,0),
	chunk_info_comp_bc numeric(11,0),
	chunk_info_comp_code numeric(6,0),
	chunk_comp_offsets bytea,
	chunk_comp_off_len numeric(11,0));

-- DROP TYPE newcollection.meta_content;

CREATE TYPE newcollection.meta_content AS (
	guid varchar(33),
	stage_num numeric(11,0),
	body bytea,
	body_full_bc numeric(11,0),
	body_comp_bc numeric(11,0),
	body_comp_code numeric(6,0),
	struct bytea,
	struct_comp_bc numeric(11,0),
	struct_comp_code numeric(6,0),
	dir_full_bc numeric(11,0),
	del_flag bpchar(1),
	reload_id numeric(11,0));

-- DROP TYPE newcollection.order_guids;

CREATE TYPE newcollection.order_guids AS (
	sequence_num numeric(1000,999),
	guid varchar);

-- DROP TYPE newcollection."_compression";

*/

/*
CREATE TYPE newcollection."_compression" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = newcollection.compression,
	DELIMITER = ',');

-- DROP TYPE newcollection."_content";

CREATE TYPE newcollection."_content" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = newcollection."content",
	DELIMITER = ',');

-- DROP TYPE newcollection."_meta_content";

CREATE TYPE newcollection."_meta_content" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = newcollection.meta_content,
	DELIMITER = ',');

-- DROP TYPE newcollection."_order_guids";


CREATE TYPE newcollection."_order_guids" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = newcollection.order_guids,
	DELIMITER = ',');
-- newcollection.compression definition
*/
-- Drop table

-- DROP TABLE newcollection.compression;

CREATE TABLE newcollection.compression (
	compression_code numeric(6) NOT NULL,
	compression_desc varchar(20) NOT NULL,
	CONSTRAINT newcollection_xpkcomp UNIQUE (compression_code)
);

-- Permissions

ALTER TABLE newcollection.compression OWNER TO postgres;
GRANT ALL ON TABLE newcollection.compression TO postgres;
GRANT SELECT ON TABLE newcollection.compression TO docread;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.compression TO docupd;
GRANT SELECT ON TABLE newcollection.compression TO novusr1;
GRANT SELECT ON TABLE newcollection.compression TO novusr2;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.compression TO novusu1;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.compression TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE newcollection.compression TO novusdocadmin;


-- newcollection."content" definition

-- Drop table

-- DROP TABLE newcollection."content";

CREATE TABLE newcollection."content" (
	guid varchar(33) NOT NULL,
	stage_num numeric(11) NOT NULL DEFAULT 0,
	body bytea NULL,
	body_full_bc numeric(11) NOT NULL DEFAULT 0,
	body_comp_bc numeric(11) NOT NULL DEFAULT 0,
	body_comp_code numeric(6) NOT NULL DEFAULT 0,
	struct bytea NULL,
	struct_comp_bc numeric(11) NOT NULL DEFAULT 0,
	struct_comp_code numeric(6) NOT NULL DEFAULT 0,
	dir_full_bc numeric(11) NOT NULL DEFAULT 0,
	wordpos_full_bc numeric(11) NULL DEFAULT 0,
	del_flag bpchar(1) NOT NULL DEFAULT 'N'::bpchar,
	include_code bpchar(1) NULL,
	reload_id numeric(11) NULL,
	chunk_count numeric(11) NULL,
	word_pos_map bytea NULL,
	word_pos_comp_bc numeric(11) NULL,
	word_pos_comp_code numeric(6) NULL,
	chunk_info bytea NULL,
	chunk_info_full_bc numeric(11) NULL,
	chunk_info_comp_bc numeric(11) NULL,
	chunk_info_comp_code numeric(6) NULL,
	chunk_comp_offsets bytea NULL,
	chunk_comp_off_len numeric(11) NULL,
	CONSTRAINT newcollection_cdfc CHECK ((del_flag = ANY (ARRAY['Y'::bpchar, 'N'::bpchar]))),
	CONSTRAINT newcollection_xpkc UNIQUE (guid, stage_num, del_flag),
	CONSTRAINT newcollection_bccc FOREIGN KEY (body_comp_code) REFERENCES newcollection.compression(compression_code),
	CONSTRAINT newcollection_sccc FOREIGN KEY (struct_comp_code) REFERENCES newcollection.compression(compression_code)
);
CREATE INDEX reload_ctt_ix ON newcollection.content USING btree (reload_id);

-- Permissions

ALTER TABLE newcollection."content" OWNER TO postgres;
GRANT ALL ON TABLE newcollection."content" TO postgres;
GRANT SELECT ON TABLE newcollection."content" TO docread;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection."content" TO docupd;
GRANT SELECT ON TABLE newcollection."content" TO novusr1;
GRANT SELECT ON TABLE newcollection."content" TO novusr2;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection."content" TO novusu1;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection."content" TO novusu2;
GRANT SELECT ON TABLE newcollection."content" TO novusdocadmin;


-- newcollection.meta_content definition

-- Drop table

-- DROP TABLE newcollection.meta_content;

CREATE TABLE newcollection.meta_content (
	guid varchar(33) NOT NULL,
	stage_num numeric(11) NOT NULL DEFAULT 0,
	body bytea NULL,
	body_full_bc numeric(11) NOT NULL DEFAULT 0,
	body_comp_bc numeric(11) NOT NULL DEFAULT 0,
	body_comp_code numeric(6) NOT NULL DEFAULT 0,
	struct bytea NULL,
	struct_comp_bc numeric(11) NOT NULL DEFAULT 0,
	struct_comp_code numeric(6) NOT NULL DEFAULT 0,
	dir_full_bc numeric(11) NOT NULL DEFAULT 0,
	del_flag bpchar(1) NOT NULL DEFAULT 'N'::bpchar,
	reload_id numeric(11) NULL,
	CONSTRAINT newcollection_cdfmc CHECK ((del_flag = ANY (ARRAY['Y'::bpchar, 'N'::bpchar]))),
	CONSTRAINT newcollection_xpkmc UNIQUE (guid, stage_num, del_flag),
	CONSTRAINT newcollection_bccmc FOREIGN KEY (body_comp_code) REFERENCES newcollection.compression(compression_code),
	CONSTRAINT newcollection_sccmc FOREIGN KEY (struct_comp_code) REFERENCES newcollection.compression(compression_code)
);
CREATE INDEX reload_mct_ix ON newcollection.meta_content USING btree (reload_id);

-- Permissions

ALTER TABLE newcollection.meta_content OWNER TO postgres;
GRANT ALL ON TABLE newcollection.meta_content TO postgres;
GRANT SELECT ON TABLE newcollection.meta_content TO docread;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.meta_content TO docupd;
GRANT SELECT ON TABLE newcollection.meta_content TO novusr1;
GRANT SELECT ON TABLE newcollection.meta_content TO novusr2;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.meta_content TO novusu1;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.meta_content TO novusu2;
GRANT SELECT ON TABLE newcollection.meta_content TO novusdocadmin;


-- newcollection.order_guids source

CREATE OR REPLACE VIEW newcollection.order_guids
AS SELECT order_guids.sequence_num,
    order_guids.guid
   FROM newcollection.order_guids() order_guids(sequence_num, guid);

-- Permissions

ALTER TABLE newcollection.order_guids OWNER TO postgres;
GRANT ALL ON TABLE newcollection.order_guids TO postgres;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.order_guids TO docread;
GRANT SELECT ON TABLE newcollection.order_guids TO novusr1;
GRANT SELECT ON TABLE newcollection.order_guids TO novusr2;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.order_guids TO novusu1;
GRANT INSERT, UPDATE, SELECT, DELETE ON TABLE newcollection.order_guids TO novusu2;
GRANT SELECT ON TABLE newcollection.order_guids TO novusdocadmin;

CREATE OR REPLACE FUNCTION newcollection.order_guids()
 RETURNS TABLE(sequence_num numeric, guid character varying)
 LANGUAGE plpgsql
AS $function$
BEGIN
BEGIN
CREATE TEMPORARY TABLE order_guids$tmp(
    sequence_num NUMERIC(11,0) NOT NULL,
    guid CHARACTER VARYING(33) NOT NULL
)
        WITH (
        OIDS=FALSE
        )
ON COMMIT DELETE ROWS;


EXCEPTION WHEN OTHERS THEN END;

RETURN QUERY SELECT * FROM order_guids$tmp;
END
$function$
;

-- Permissions

ALTER FUNCTION newcollection.order_guids() OWNER TO postgres;
GRANT ALL ON FUNCTION newcollection.order_guids() TO postgres;

CREATE OR REPLACE FUNCTION newcollection.order_guids_iud()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
BEGIN
BEGIN
CREATE TEMPORARY TABLE order_guids$tmp(
    sequence_num NUMERIC(11,0) NOT NULL,
    guid CHARACTER VARYING(33) NOT NULL
)
        WITH (
        OIDS=FALSE
        )
ON COMMIT DELETE ROWS;


EXCEPTION WHEN OTHERS THEN END;

IF tg_op = 'INSERT' THEN 
INSERT INTO order_guids$tmp(sequence_num,guid)
 VALUES (new.sequence_num,new.guid) RETURNING * INTO NEW;
RETURN new;
ELSIF tg_op = 'UPDATE' THEN 
UPDATE order_guids$tmp
 SET sequence_num=new.sequence_num, guid=new.guid 
WHERE sequence_num=old.sequence_num AND guid=old.guid RETURNING * INTO NEW;
RETURN new;
ELSIF tg_op = 'DELETE' THEN 
DELETE FROM order_guids$tmp 
WHERE sequence_num=old.sequence_num AND guid=old.guid; 
RETURN old;
END IF;
END
$function$
;

-- Permissions

ALTER FUNCTION newcollection.order_guids_iud() OWNER TO postgres;
GRANT ALL ON FUNCTION newcollection.order_guids_iud() TO postgres;


-- Permissions

GRANT ALL ON SCHEMA newcollection TO postgres;
GRANT USAGE ON SCHEMA newcollection TO novusu1;
GRANT USAGE ON SCHEMA newcollection TO novusu2;
GRANT USAGE ON SCHEMA newcollection TO novusr1;
GRANT USAGE ON SCHEMA newcollection TO novusr2;
GRANT USAGE ON SCHEMA newcollection TO maverickr;
GRANT USAGE ON SCHEMA newcollection TO datadog;
GRANT USAGE ON SCHEMA newcollection TO novusdocadmin;
GRANT TRUNCATE ON SCHEMA newcollection TO novusdocadmin;
