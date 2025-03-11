delete from sys_user where id in (1001,1002,1003,1004,1005,1006,1007,1008,1009,1010);
delete from sys_user_role where user_id in (1001,1002,1003,1004,1005,1006,1007,1008,1009,1010);
delete from sys_user_position where user_id in (1001,1002,1003,1004,1005,1006,1007,1008,1009,1010);
delete from sys_user_position where user_id in (1001,1002,1003,1004,1005,1006,1007,1008,1009,1010);

INSERT INTO sys_user (id, login_name, password, name, sex, avatar, mobile, department_id, duty, status, operator_id, modify_time, create_time, is_system, login_ip, login_time, login_success, login_err_count, locked, emp_id, woker_no, parent_id) VALUES
(1001, 'sqr', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '申请人ldk', 3, NULL, NULL, 1536265613394063361, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1002, 'zb-jl', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '责任部值班经理ldk', 3, NULL, NULL, 1536265613394063361, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1003, 'aj-jl', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '责任部门安质经理ldk', 3, NULL, NULL, 1536265613394063361, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1004, 'aj-jb', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '安监值班ldk', 3, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1005, 'aj-jcy', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '安监监察员ldk', 3, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1006, 'aj-jcy2', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '安监监察员2ldk', 3, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1007, 'ajld', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '安监领导ldk', 3, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1008, 'ajld2', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '安监领导2ldk', 3, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1009, 'aqxxy', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '安全信息员ldk', 3, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1),
(1010, 'aqxxy2', '$2a$10$ijVVERAa5GGwVkjCjFSdZ..3ruzNxt4Enm1fuw/MaEn8ZGgLFUX3i', '安全信息员2ldk', 3, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 0, NULL, NULL, 1, 0, 0, NULL, NULL,1);

INSERT INTO sys_user_role (id, user_id, role_id) VALUES
(100001, 1001, 2),
(100002, 1002, 2),
(100003, 1003, 2),
(100004, 1004, 2),
(100005, 1005, 2),
(100006, 1006, 2),
(100007, 1007, 2),
(100008, 1008, 2),
(100009, 1009, 2),
(100010, 1010, 2);

INSERT INTO sys_user_position (id, user_id, position_id) VALUES
(100001, 1002, 7),
(100002, 1003, 3),
(100003, 1004, 8),
(100004, 1005, 9),
(100005, 1006, 9),
(100006, 1007, 15),
(100007, 1008, 15),
(100008, 1009, 10),
(100009, 1010, 10);


