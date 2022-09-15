-- DROP SCHEMA [NEWCOLLNAME];

CREATE SCHEMA [NEWCOLLNAME] AUTHORIZATION postgres;

-- DROP TYPE [NEWCOLLNAME].compression;

CREATE TYPE [NEWCOLLNAME].compression AS (
	compression_code numeric(6,0),
	compression_desc varchar(20));

-- DROP TYPE [NEWCOLLNAME]."content";

CREATE TYPE [NEWCOLLNAME]."content" AS (
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

-- DROP TYPE [NEWCOLLNAME].meta_content;

CREATE TYPE [NEWCOLLNAME].meta_content AS (
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

-- DROP TYPE [NEWCOLLNAME].order_guids;

CREATE TYPE [NEWCOLLNAME].order_guids AS (
	sequence_num numeric(1000,999),
	guid varchar);

-- DROP TYPE [NEWCOLLNAME]."_compression";

-- DO NOT CREATE BASE TYPES: SUPERUSER UNAVAILABLE IN AWS RDS
/*
CREATE TYPE [NEWCOLLNAME]."_compression" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = [NEWCOLLNAME].compression,
	DELIMITER = ',');

-- DROP TYPE [NEWCOLLNAME]."_content";

CREATE TYPE [NEWCOLLNAME]."_content" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = [NEWCOLLNAME]."content",
	DELIMITER = ',');

-- DROP TYPE [NEWCOLLNAME]."_meta_content";

CREATE TYPE [NEWCOLLNAME]."_meta_content" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = [NEWCOLLNAME].meta_content,
	DELIMITER = ',');

-- DROP TYPE [NEWCOLLNAME]."_order_guids";

CREATE TYPE [NEWCOLLNAME]."_order_guids" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = [NEWCOLLNAME].order_guids,
	DELIMITER = ',');
-- [NEWCOLLNAME].compression definition

*/

-- Drop table

-- DROP TABLE [NEWCOLLNAME].compression;

CREATE TABLE [NEWCOLLNAME].compression (
	compression_code numeric(6) NOT NULL,
	compression_desc varchar(20) NOT NULL,
	CONSTRAINT [NEWCOLLNAME]_xpkcomp UNIQUE (compression_code)
);

-- Permissions

ALTER TABLE [NEWCOLLNAME].compression OWNER TO postgres;
GRANT ALL ON TABLE [NEWCOLLNAME].compression TO postgres;
GRANT SELECT ON TABLE [NEWCOLLNAME].compression TO docread;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].compression TO docupd;
GRANT SELECT ON TABLE [NEWCOLLNAME].compression TO novusr1;
GRANT SELECT ON TABLE [NEWCOLLNAME].compression TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].compression TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].compression TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE [NEWCOLLNAME].compression TO novusdocadmin;


-- [NEWCOLLNAME]."content" definition

-- Drop table

-- DROP TABLE [NEWCOLLNAME]."content";

CREATE TABLE [NEWCOLLNAME]."content" (
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
	CONSTRAINT [NEWCOLLNAME]_cdfc CHECK ((del_flag = ANY (ARRAY['Y'::bpchar, 'N'::bpchar]))),
	CONSTRAINT [NEWCOLLNAME]_xpkc UNIQUE (guid, stage_num, del_flag),
	CONSTRAINT [NEWCOLLNAME]_bccc FOREIGN KEY (body_comp_code) REFERENCES [NEWCOLLNAME].compression(compression_code),
	CONSTRAINT [NEWCOLLNAME]_sccc FOREIGN KEY (struct_comp_code) REFERENCES [NEWCOLLNAME].compression(compression_code)
);
CREATE INDEX reload_ctt_ix ON [NEWCOLLNAME].content USING btree (reload_id);

-- Permissions

ALTER TABLE [NEWCOLLNAME]."content" OWNER TO postgres;
GRANT ALL ON TABLE [NEWCOLLNAME]."content" TO postgres;
GRANT SELECT ON TABLE [NEWCOLLNAME]."content" TO docread;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME]."content" TO docupd;
GRANT SELECT ON TABLE [NEWCOLLNAME]."content" TO novusr1;
GRANT SELECT ON TABLE [NEWCOLLNAME]."content" TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME]."content" TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME]."content" TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE [NEWCOLLNAME]."content" TO novusdocadmin;


-- [NEWCOLLNAME].meta_content definition

-- Drop table

-- DROP TABLE [NEWCOLLNAME].meta_content;

CREATE TABLE [NEWCOLLNAME].meta_content (
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
	CONSTRAINT [NEWCOLLNAME]_cdfmc CHECK ((del_flag = ANY (ARRAY['Y'::bpchar, 'N'::bpchar]))),
	CONSTRAINT [NEWCOLLNAME]_xpkmc UNIQUE (guid, stage_num, del_flag),
	CONSTRAINT [NEWCOLLNAME]_bccmc FOREIGN KEY (body_comp_code) REFERENCES [NEWCOLLNAME].compression(compression_code),
	CONSTRAINT [NEWCOLLNAME]_sccmc FOREIGN KEY (struct_comp_code) REFERENCES [NEWCOLLNAME].compression(compression_code)
);
CREATE INDEX reload_mct_ix ON [NEWCOLLNAME].meta_content USING btree (reload_id);

-- Permissions

ALTER TABLE [NEWCOLLNAME].meta_content OWNER TO postgres;
GRANT ALL ON TABLE [NEWCOLLNAME].meta_content TO postgres;
GRANT SELECT ON TABLE [NEWCOLLNAME].meta_content TO docread;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].meta_content TO docupd;
GRANT SELECT ON TABLE [NEWCOLLNAME].meta_content TO novusr1;
GRANT SELECT ON TABLE [NEWCOLLNAME].meta_content TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].meta_content TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].meta_content TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE [NEWCOLLNAME].meta_content TO novusdocadmin;


-- [NEWCOLLNAME].order_guids source

CREATE OR REPLACE VIEW [NEWCOLLNAME].order_guids
AS SELECT order_guids.sequence_num,
    order_guids.guid
   FROM [NEWCOLLNAME].order_guids() order_guids(sequence_num, guid);

-- Permissions

ALTER TABLE [NEWCOLLNAME].order_guids OWNER TO postgres;
GRANT ALL ON TABLE [NEWCOLLNAME].order_guids TO postgres;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].order_guids TO docread;
GRANT SELECT ON TABLE [NEWCOLLNAME].order_guids TO novusr1;
GRANT SELECT ON TABLE [NEWCOLLNAME].order_guids TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].order_guids TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE [NEWCOLLNAME].order_guids TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE [NEWCOLLNAME].order_guids TO novusdocadmin;



CREATE OR REPLACE FUNCTION [NEWCOLLNAME].order_guids()
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

ALTER FUNCTION [NEWCOLLNAME].order_guids() OWNER TO postgres;
GRANT ALL ON FUNCTION [NEWCOLLNAME].order_guids() TO postgres;

CREATE OR REPLACE FUNCTION [NEWCOLLNAME].order_guids_iud()
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

ALTER FUNCTION [NEWCOLLNAME].order_guids_iud() OWNER TO postgres;
GRANT ALL ON FUNCTION [NEWCOLLNAME].order_guids_iud() TO postgres;


-- Permissions

GRANT ALL ON SCHEMA [NEWCOLLNAME] TO postgres;
GRANT USAGE ON SCHEMA [NEWCOLLNAME] TO novusu1;
GRANT USAGE ON SCHEMA [NEWCOLLNAME] TO novusu2;
GRANT USAGE ON SCHEMA [NEWCOLLNAME] TO novusr1;
GRANT USAGE ON SCHEMA [NEWCOLLNAME] TO novusr2;
GRANT USAGE ON SCHEMA [NEWCOLLNAME] TO maverickr;
GRANT USAGE ON SCHEMA [NEWCOLLNAME] TO datadog;
GRANT USAGE ON SCHEMA [NEWCOLLNAME] TO novusdocadmin;
