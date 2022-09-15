CREATE ROLE novus_admin WITH PASSWORD 'asadmin' CREATEDB CREATEROLE LOGIN;

GRANT rds_superuser TO novus_admin;
GRANT postgres TO novus_admin;

SELECT rolname, usename FROM pg_user
JOIN pg_auth_members ON pg_user.usesysid = pg_auth_members.member
JOIN pg_roles ON pg_roles.oid = pg_auth_members.roleid
WHERE pg_roles.rolname = 'rds_superuser';