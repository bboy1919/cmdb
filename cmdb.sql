/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : cmdb

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2019-06-05 11:54:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('db9319e25d39');

-- ----------------------------
-- Table structure for cabinet
-- ----------------------------
DROP TABLE IF EXISTS `cabinet`;
CREATE TABLE `cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `idc_id` int(11) DEFAULT NULL,
  `power` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idc_id` (`idc_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of cabinet
-- ----------------------------
INSERT INTO `cabinet` VALUES ('1', '1-1', '13', '42');
INSERT INTO `cabinet` VALUES ('2', '1-2', '15', '21');

-- ----------------------------
-- Table structure for idc
-- ----------------------------
DROP TABLE IF EXISTS `idc`;
CREATE TABLE `idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `idc_name` varchar(30) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  `user_interface` varchar(50) NOT NULL,
  `user_phone` varchar(20) NOT NULL,
  `rel_cabinet_num` varchar(11) DEFAULT NULL,
  `pact_cabinet_num` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of idc
-- ----------------------------
INSERT INTO `idc` VALUES ('13', '易信东莞', '易信科技东莞樟木头', '樟木头镇银河北路中国电信', '13484829392', 'chaor29@sina.com', '刘飞', '13484829392', '20', '11');
INSERT INTO `idc` VALUES ('15', '易信长沙', '长沙麓谷机房一期', '长沙市麓谷高新区桐梓坡西路', '13958439821', 'djjie@in.com', '陈一', '13958439821', '40', '23');

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `name_cn` varchar(40) NOT NULL,
  `url` varchar(128) NOT NULL,
  `comment` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of permission
-- ----------------------------
INSERT INTO `permission` VALUES ('4', 'git', 'git仓库', '/project/project', '测试');
INSERT INTO `permission` VALUES ('14', 'cobbler', '装机平台', '/cobbler', '赋予装机平台权限');
INSERT INTO `permission` VALUES ('6', 'zabbix', '监控', '/zabbix', '监控管理');
INSERT INTO `permission` VALUES ('7', 'elk', '性能展示', '/show', '性能展示');
INSERT INTO `permission` VALUES ('8', 'testing', '测试发布', '/project/testing', '代码测试发布');
INSERT INTO `permission` VALUES ('9', 'applye', '申请发布', '/proect/apply', '申请发布sss');
INSERT INTO `permission` VALUES ('10', 'deploy', '发布列表', '/proect/deploy', '发布列表');
INSERT INTO `permission` VALUES ('15', 'cmdb', '资产管理', '/cmdb', 'CMDB管理');
INSERT INTO `permission` VALUES ('16', 'device', '设备保障', '/device', '设备保障申请，需由管理员进行下架协调');
INSERT INTO `permission` VALUES ('17', 'report', '申请报障', '/device/report', '可以进行故障申报');
INSERT INTO `permission` VALUES ('18', 'maintain', '故障处理', '/device/maintain', '管理员权限故障处理');
INSERT INTO `permission` VALUES ('19', 'down', '下架服务器查看', '/device/down', '下架服务器查看');
INSERT INTO `permission` VALUES ('21', 'user', '用户权限管理', '/user', '用户权限管理');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `name_cn` varchar(40) NOT NULL,
  `info` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('1', 'sa', '运维组', '超级管理员');
INSERT INTO `role` VALUES ('10', 'zj', '装机', '专门装机用户');
INSERT INTO `role` VALUES ('11', 'zabbix', '监控用户组', '监控用户组合管理员组');
INSERT INTO `role` VALUES ('12', 'cmdb', 'cmdb管理组', '资产管理和审计');
INSERT INTO `role` VALUES ('13', 'device', '设备保障组', '设备保障');
INSERT INTO `role` VALUES ('14', 'report', '故障申报2', '普通用户故障申报');
INSERT INTO `role` VALUES ('15', 'maintain', '管理员故障处理', '管理员拥有故障处理功能');
INSERT INTO `role` VALUES ('20', 'cse', '色非', '色鬼');

-- ----------------------------
-- Table structure for role_o2m_permission
-- ----------------------------
DROP TABLE IF EXISTS `role_o2m_permission`;
CREATE TABLE `role_o2m_permission` (
  `role_id` int(11) DEFAULT NULL,
  `permission_id` int(11) DEFAULT NULL,
  KEY `role_id` (`role_id`),
  KEY `permission_id` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role_o2m_permission
-- ----------------------------
INSERT INTO `role_o2m_permission` VALUES ('1', '4');
INSERT INTO `role_o2m_permission` VALUES ('1', '14');
INSERT INTO `role_o2m_permission` VALUES ('1', '1');
INSERT INTO `role_o2m_permission` VALUES ('1', '6');
INSERT INTO `role_o2m_permission` VALUES ('1', '7');
INSERT INTO `role_o2m_permission` VALUES ('1', '8');
INSERT INTO `role_o2m_permission` VALUES ('1', '9');
INSERT INTO `role_o2m_permission` VALUES ('1', '10');
INSERT INTO `role_o2m_permission` VALUES ('1', '15');
INSERT INTO `role_o2m_permission` VALUES ('12', '15');
INSERT INTO `role_o2m_permission` VALUES ('15', '18');
INSERT INTO `role_o2m_permission` VALUES ('15', '19');
INSERT INTO `role_o2m_permission` VALUES ('13', '8');
INSERT INTO `role_o2m_permission` VALUES ('13', '7');
INSERT INTO `role_o2m_permission` VALUES ('11', '6');
INSERT INTO `role_o2m_permission` VALUES ('20', '21');
INSERT INTO `role_o2m_permission` VALUES ('1', '21');

-- ----------------------------
-- Table structure for server
-- ----------------------------
DROP TABLE IF EXISTS `server`;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(20) DEFAULT NULL,
  `ip` varchar(20) DEFAULT NULL,
  `vm_status` int(11) DEFAULT NULL,
  `st` varchar(50) DEFAULT NULL,
  `uuid` varchar(100) DEFAULT NULL,
  `manufacturers` varchar(100) DEFAULT NULL,
  `server_type` varchar(200) DEFAULT NULL,
  `server_cpu` varchar(200) DEFAULT NULL,
  `os` varchar(30) DEFAULT NULL,
  `server_disk` varchar(20) DEFAULT NULL,
  `mac_address` varchar(30) DEFAULT NULL,
  `supplier` varchar(30) DEFAULT NULL,
  `cab_id` int(11) DEFAULT NULL,
  `cab_pos` varchar(10) DEFAULT NULL,
  `supplier_phone` varchar(20) DEFAULT NULL,
  `server_purpose` varchar(30) DEFAULT NULL,
  `host` int(11) DEFAULT NULL,
  `server_run` varchar(30) DEFAULT NULL,
  `host_status` int(11) DEFAULT NULL,
  `host_models` varchar(10) DEFAULT NULL,
  `expire` date DEFAULT NULL,
  `manufacture_date` date DEFAULT NULL,
  `server_up_time` date DEFAULT NULL,
  `server_mem` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cab_id` (`cab_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of server
-- ----------------------------
INSERT INTO `server` VALUES ('1', 'nginx-1', '10.0.0.81', '1', 'FJ2SHY1', '4C4C4544-004A-3210-8053-C6C04F485931', '戴尔（DELL）', '戴尔2U机架式服务器主机R730', '英特尔至强处理器', 'CentOS', '300G', '00-01-6C-06-A6-29 ', '戴尔', '2', '2', '0102948482', '1', '3', '2', null, '', '2019-07-11', '2016-07-11', '2019-04-30', '8');
INSERT INTO `server` VALUES ('2', 'nginx-12', '10.0.0.33', '1', '', '4C4C4544-004A-3310-8053-C6C04F485931', '戴尔（DELL）', '戴尔2U机架式服务器主机R730', '英特尔至强处理器', 'CentOS', '300G', '00-01-64-06-A6-29 ', '戴尔', '2', '1', '0102948482', '1', '2', '2', '1', '', '2019-07-19', null, '2019-04-15', null);

-- ----------------------------
-- Table structure for switch
-- ----------------------------
DROP TABLE IF EXISTS `switch`;
CREATE TABLE `switch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(50) DEFAULT NULL,
  `device` varchar(40) NOT NULL,
  `port` int(11) DEFAULT NULL,
  `cab_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cab_id` (`cab_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of switch
-- ----------------------------
INSERT INTO `switch` VALUES ('1', '192.168.1.212', '华为（HUAWEI）S5720S-28P-SI-AC', '22', '1');
INSERT INTO `switch` VALUES ('2', '192.168.1.123', '华三（H3C）S1850-28P-PWR', '32', '2');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `join_date` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `password` varchar(128) DEFAULT NULL,
  `name` varchar(80) NOT NULL,
  `mobile` varchar(16) DEFAULT NULL,
  `is_lock` int(11) NOT NULL,
  `last_login` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1558323282', '1', '1', 'nc1919', 'pbkdf2:sha256:150000$ToOeytii$4b570e5df69b978177796d39b5bc466258efd37532d1d2b01d860d8391e4a2ff', '金角大王', '15068017271', '1', '1558831766');
INSERT INTO `user` VALUES ('1559614779', '1', '17', 'ccoe1919', 'pbkdf2:sha256:150000$Bu6NtFqN$47c2b4ca5e50147bb6bc00943aec72dec00d6de837cffab3064bf47fc583abc3', '老男孩', '13545645324', '0', '1559702688');
INSERT INTO `user` VALUES ('1558605935', '1', '4', 'admin', 'pbkdf2:sha256:150000$D0sIalhx$b2e2ce9f5ce4f3d808d6dd123eca25a81c19964990efbe214bc4f6c4579fbc6d', '教育', '13545645324', '0', '1559701844');
INSERT INTO `user` VALUES ('1559614821', '0', '18', 'bboy2002', 'pbkdf2:sha256:150000$JF8DIgy0$91a49992ceeb984718e05f813d8dace286068a29cb5676b3d137d658dead27f4', '中华有', '13545645324', '0', null);
INSERT INTO `user` VALUES ('1558772623', '1', '6', 'roote', 'pbkdf2:sha256:150000$fkjy5e2R$fbb2bb13870e368f64516f781f46ea80afdba90908491920406288292f8da75d', '小白', '15068017271', '0', '1559647751');
INSERT INTO `user` VALUES ('1559614880', '0', '19', 'nc2002', 'pbkdf2:sha256:150000$6X0pwxnM$7a74601a31b6522d1462a90ced0cd39268c9643fb8998570b2a97bee313f4b95', '刘飞', '13545645324', '0', null);

-- ----------------------------
-- Table structure for user_o2m_role
-- ----------------------------
DROP TABLE IF EXISTS `user_o2m_role`;
CREATE TABLE `user_o2m_role` (
  `u_id` int(11) DEFAULT NULL,
  `r_id` int(11) DEFAULT NULL,
  KEY `u_id` (`u_id`),
  KEY `r_id` (`r_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user_o2m_role
-- ----------------------------
INSERT INTO `user_o2m_role` VALUES ('1', '12');
INSERT INTO `user_o2m_role` VALUES ('7', '13');
INSERT INTO `user_o2m_role` VALUES ('1', '13');
INSERT INTO `user_o2m_role` VALUES ('1', '14');
INSERT INTO `user_o2m_role` VALUES ('1', '10');
INSERT INTO `user_o2m_role` VALUES ('7', '12');
INSERT INTO `user_o2m_role` VALUES ('5', '11');
INSERT INTO `user_o2m_role` VALUES ('2', '12');
INSERT INTO `user_o2m_role` VALUES ('5', '12');
INSERT INTO `user_o2m_role` VALUES ('5', '1');
INSERT INTO `user_o2m_role` VALUES ('6', '1');
INSERT INTO `user_o2m_role` VALUES ('6', '11');
INSERT INTO `user_o2m_role` VALUES ('4', '1');
INSERT INTO `user_o2m_role` VALUES ('8', '11');
INSERT INTO `user_o2m_role` VALUES ('9', '10');
INSERT INTO `user_o2m_role` VALUES ('9', '12');
INSERT INTO `user_o2m_role` VALUES ('10', '10');
INSERT INTO `user_o2m_role` VALUES ('11', '12');
INSERT INTO `user_o2m_role` VALUES ('12', '12');
INSERT INTO `user_o2m_role` VALUES ('13', '11');
INSERT INTO `user_o2m_role` VALUES ('11', '10');
INSERT INTO `user_o2m_role` VALUES ('14', '10');
INSERT INTO `user_o2m_role` VALUES ('14', '12');
INSERT INTO `user_o2m_role` VALUES ('15', '10');
INSERT INTO `user_o2m_role` VALUES ('15', '11');
INSERT INTO `user_o2m_role` VALUES ('16', '11');
INSERT INTO `user_o2m_role` VALUES ('16', '12');
INSERT INTO `user_o2m_role` VALUES ('18', '1');
INSERT INTO `user_o2m_role` VALUES ('19', '14');
INSERT INTO `user_o2m_role` VALUES ('17', '13');
INSERT INTO `user_o2m_role` VALUES ('6', '15');

-- ----------------------------
-- Table structure for zbhost
-- ----------------------------
DROP TABLE IF EXISTS `zbhost`;
CREATE TABLE `zbhost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cmdb_hostid` int(11) DEFAULT NULL,
  `hostid` int(11) DEFAULT NULL,
  `host` varchar(40) DEFAULT NULL,
  `ip` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=239 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of zbhost
-- ----------------------------
INSERT INTO `zbhost` VALUES ('236', null, '10084', 'Zabbix server', '127.0.0.1');
INSERT INTO `zbhost` VALUES ('237', null, '10105', 'web-01', '10.0.0.8');
INSERT INTO `zbhost` VALUES ('238', null, '10106', 'db-01', '10.0.0.51');
