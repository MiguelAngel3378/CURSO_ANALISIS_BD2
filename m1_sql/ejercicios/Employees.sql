-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema DB_employees
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `DB_employees` ;

-- -----------------------------------------------------
-- Schema DB_employees
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DB_employees` DEFAULT CHARACTER SET utf8 ;
USE `DB_employees` ;

-- -----------------------------------------------------
-- Table `DB_employees`.`Company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_employees`.`Company` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Adress` VARCHAR(45) NULL,
  `Phone` VARCHAR(9) NULL,
  `Ciif` VARCHAR(10) NULL,
  `Foundation_year` YEAR(5) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Ciif_UNIQUE` ON `DB_employees`.`Company` (`Ciif` ASC) VISIBLE;

CREATE UNIQUE INDEX `Phone_UNIQUE` ON `DB_employees`.`Company` (`Phone` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `DB_employees`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_employees`.`Employee` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `First_name` VARCHAR(45) NULL,
  `Last_name` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `Available` BIT(1) NOT NULL,
  `Job_role` VARCHAR(45) NULL,
  `Job_label` VARCHAR(45) NULL,
  `Nif` VARCHAR(9) NULL,
  `Company_id` INT(9) NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `Fk_employee_company`
    FOREIGN KEY (`Company_id`)
    REFERENCES `DB_employees`.`Company` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Phone_UNIQUE` ON `DB_employees`.`Employee` (`Phone` ASC) VISIBLE;

CREATE INDEX `Fk_employee_company_idx` ON `DB_employees`.`Employee` (`Company_id` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `DB_employees`.`Company`
-- -----------------------------------------------------
START TRANSACTION;
USE `DB_employees`;
INSERT INTO `DB_employees`.`Company` (`ID`, `Name`, `Adress`, `Phone`, `Ciif`, `Foundation_year`) VALUES (, 'Fundacion Adecco', 'Avenida Principe Pio 110', '6562789', 'UV10001', 1990);
INSERT INTO `DB_employees`.`Company` (`ID`, `Name`, `Adress`, `Phone`, `Ciif`, `Foundation_year`) VALUES (, 'Fundacion Telefonica', 'Avenida Ronda de la Comunicacion NN', '6572890', 'UV10002', 1976);

COMMIT;


-- -----------------------------------------------------
-- Data for table `DB_employees`.`Employee`
-- -----------------------------------------------------
START TRANSACTION;
USE `DB_employees`;
INSERT INTO `DB_employees`.`Employee` (`ID`, `First_name`, `Last_name`, `Phone`, `Available`, `Job_role`, `Job_label`, `Nif`, `Company_id`) VALUES (DEFAULT, 'Miguel Angel', 'Suarez', '680924086', 1, 'Analitics', 'Metadatos', 'Y8767370Z', 10);
INSERT INTO `DB_employees`.`Employee` (`ID`, `First_name`, `Last_name`, `Phone`, `Available`, `Job_role`, `Job_label`, `Nif`, `Company_id`) VALUES (DEFAULT, 'Enrique Alberto', 'Suarez', '680934086', 1, 'Developer', 'DataBase', 'Y8867370Z', 10);
INSERT INTO `DB_employees`.`Employee` (`ID`, `First_name`, `Last_name`, `Phone`, `Available`, `Job_role`, `Job_label`, `Nif`, `Company_id`) VALUES (DEFAULT, 'David', 'Suarez', '680944086', 1, 'Config', 'Logistic', NULL, 20);

COMMIT;

