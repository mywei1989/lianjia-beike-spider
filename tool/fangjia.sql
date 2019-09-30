/*
 Navicat Premium Data Transfer

 Source Server         : 185.241.43.8
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : 185.241.43.8:13306
 Source Schema         : fangjia

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 30/09/2019 16:10:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for xiaoqu_info
-- ----------------------------
DROP TABLE IF EXISTS `xiaoqu_info`;
CREATE TABLE `xiaoqu_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `city` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `district` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `area` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `xiaoqu` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_city_district_xiaoqu`(`city`, `district`, `area`, `xiaoqu`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9961 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for xiaoqu_price
-- ----------------------------
DROP TABLE IF EXISTS `xiaoqu_price`;
CREATE TABLE `xiaoqu_price`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `xiaoqu_info_id` bigint(20) NULL DEFAULT NULL,
  `date` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `district` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `area` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `xiaoqu` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `price` int(11) NULL DEFAULT NULL,
  `sale` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_date`(`date`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 99656 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
