SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `login04` (
  `id` int NOT NULL,
  `name04` varchar(255) NOT NULL,
  `pass04` varchar(255) DEFAULT NULL,
  `email04` varchar(255) NOT NULL
) ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `login04`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `login04`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
