--DROP SCHEMA w3rdstaidnv23;

CREATE SCHEMA w3rdstaidnv23 AUTHORIZATION postgres;

-- Drop table

-- DROP TABLE w3rdstaidnv23.compression;

CREATE TABLE w3rdstaidnv23.compression (
	compression_code numeric(6) NOT NULL,
	compression_desc varchar(20) NOT NULL,
	CONSTRAINT w3rdstaidnv23_xpkcomp UNIQUE (compression_code)
);

-- Permissions

ALTER TABLE w3rdstaidnv23.compression OWNER TO postgres;
GRANT ALL ON TABLE w3rdstaidnv23.compression TO postgres;
GRANT SELECT ON TABLE w3rdstaidnv23.compression TO docread;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.compression TO docupd;
GRANT SELECT ON TABLE w3rdstaidnv23.compression TO novusr1;
GRANT SELECT ON TABLE w3rdstaidnv23.compression TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.compression TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.compression TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE w3rdstaidnv23.compression TO novusdocadmin;


-- w3rdstaidnv23.wpos definition

-- Drop table

-- DROP TABLE w3rdstaidnv23.wpos;

CREATE TABLE w3rdstaidnv23.wpos (
	guid varchar(33) NOT NULL,
	collection_id numeric(11) NOT NULL,
	stage_num numeric(11) NOT NULL,
	del_flag bpchar(1) NOT NULL,
	word_pos_map bytea NULL,
	wordpos_full_bc numeric(11) NULL,
	word_pos_comp_bc numeric(11) NULL,
	word_pos_comp_code numeric(6) NULL,
	reload_id numeric(11) NULL,
	CONSTRAINT w3rdstaidnv23_pk_wpos PRIMARY KEY (guid, collection_id, stage_num, del_flag)
);

-- Permissions

ALTER TABLE w3rdstaidnv23.wpos OWNER TO postgres;
GRANT ALL ON TABLE w3rdstaidnv23.wpos TO postgres;
GRANT SELECT ON TABLE w3rdstaidnv23.wpos TO docread;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.wpos TO docupd;
GRANT SELECT ON TABLE w3rdstaidnv23.wpos TO novusr1;
GRANT SELECT ON TABLE w3rdstaidnv23.wpos TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.wpos TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.wpos TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE w3rdstaidnv23.wpos TO novusdocadmin;


-- w3rdstaidnv23."content" definition

-- Drop table

-- DROP TABLE w3rdstaidnv23."content";

CREATE TABLE w3rdstaidnv23."content" (
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
	CONSTRAINT w3rdstaidnv23_cdfc CHECK ((del_flag = ANY (ARRAY['Y'::bpchar, 'N'::bpchar]))),
	CONSTRAINT w3rdstaidnv23_xpkc UNIQUE (guid, stage_num, del_flag),
	CONSTRAINT w3rdstaidnv23_bccc FOREIGN KEY (body_comp_code) REFERENCES w3rdstaidnv23.compression(compression_code),
	CONSTRAINT w3rdstaidnv23_sccc FOREIGN KEY (struct_comp_code) REFERENCES w3rdstaidnv23.compression(compression_code)
);
CREATE INDEX reload_ctt_ix ON w3rdstaidnv23.content USING btree (reload_id);

-- Permissions

ALTER TABLE w3rdstaidnv23."content" OWNER TO postgres;
GRANT ALL ON TABLE w3rdstaidnv23."content" TO postgres;
GRANT SELECT ON TABLE w3rdstaidnv23."content" TO docread;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23."content" TO docupd;
GRANT SELECT ON TABLE w3rdstaidnv23."content" TO novusr1;
GRANT SELECT ON TABLE w3rdstaidnv23."content" TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23."content" TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23."content" TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE w3rdstaidnv23."content" TO novusdocadmin;


-- w3rdstaidnv23.meta_content definition

-- Drop table

-- DROP TABLE w3rdstaidnv23.meta_content;

CREATE TABLE w3rdstaidnv23.meta_content (
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
	CONSTRAINT w3rdstaidnv23_cdfmc CHECK ((del_flag = ANY (ARRAY['Y'::bpchar, 'N'::bpchar]))),
	CONSTRAINT w3rdstaidnv23_xpkmc UNIQUE (guid, stage_num, del_flag),
	CONSTRAINT w3rdstaidnv23_bccmc FOREIGN KEY (body_comp_code) REFERENCES w3rdstaidnv23.compression(compression_code),
	CONSTRAINT w3rdstaidnv23_sccmc FOREIGN KEY (struct_comp_code) REFERENCES w3rdstaidnv23.compression(compression_code)
);
CREATE INDEX reload_mct_ix ON w3rdstaidnv23.meta_content USING btree (reload_id);

-- Permissions

ALTER TABLE w3rdstaidnv23.meta_content OWNER TO postgres;
GRANT ALL ON TABLE w3rdstaidnv23.meta_content TO postgres;
GRANT SELECT ON TABLE w3rdstaidnv23.meta_content TO docread;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.meta_content TO docupd;
GRANT SELECT ON TABLE w3rdstaidnv23.meta_content TO novusr1;
GRANT SELECT ON TABLE w3rdstaidnv23.meta_content TO novusr2;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.meta_content TO novusu1;
GRANT DELETE, SELECT, UPDATE, INSERT ON TABLE w3rdstaidnv23.meta_content TO novusu2;
GRANT SELECT, TRUNCATE ON TABLE w3rdstaidnv23.meta_content TO novusdocadmin;




-- Permissions

GRANT ALL ON SCHEMA w3rdstaidnv23 TO postgres;
GRANT USAGE ON SCHEMA w3rdstaidnv23 TO novusu1;
GRANT USAGE ON SCHEMA w3rdstaidnv23 TO novusu2;
GRANT USAGE ON SCHEMA w3rdstaidnv23 TO novusr1;
GRANT USAGE ON SCHEMA w3rdstaidnv23 TO novusr2;
GRANT USAGE ON SCHEMA w3rdstaidnv23 TO maverickr;
GRANT USAGE ON SCHEMA w3rdstaidnv23 TO datadog;
GRANT USAGE ON SCHEMA w3rdstaidnv23 TO novusdocadmin;
