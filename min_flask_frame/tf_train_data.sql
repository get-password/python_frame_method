/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50734
 Source Host           : localhost:3306
 Source Schema         : tf_train_data

 Target Server Type    : MySQL
 Target Server Version : 50734
 File Encoding         : 65001

 Date: 21/07/2021 21:02:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for train_info
-- ----------------------------
DROP TABLE IF EXISTS `train_info`;
CREATE TABLE `train_info`  (
  `id` bigint(100) NOT NULL AUTO_INCREMENT,
  `dataset_name` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `method` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `accuracy` float(20, 0) NULL DEFAULT NULL,
  `loss` float(20, 0) NOT NULL,
  `illustrate` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `state` tinyint(1) NOT NULL DEFAULT 1,
  `update_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `creat_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of train_info
-- ----------------------------
INSERT INTO `train_info` VALUES (1, 'boshidun', 'vgg16', NULL, 10, '这是一个测试', 1, '2021-07-18 19:01:56', '2021-07-07 18:09:27');

SET FOREIGN_KEY_CHECKS = 1;
