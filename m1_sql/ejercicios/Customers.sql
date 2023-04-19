CREATE TABLE `customers` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `last-name` varchar(45) DEFAULT NULL,
  `nif` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nif_UNIQUE` (`nif`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci