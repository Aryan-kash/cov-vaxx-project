-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 30, 2023 at 01:52 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vaccine`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookingslot`
--

CREATE TABLE `bookingslot` (
  `id` int(11) NOT NULL,
  `adhaar` varchar(20) NOT NULL,
  `centrecode` varchar(20) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `pphone` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookingslot`
--

INSERT INTO `bookingslot` (`id`, `adhaar`, `centrecode`, `pname`, `pphone`) VALUES
(1, ' 987654321', '1234', 'Aryan', '7002834442'),
(2, ' 111222333', '5678', 'Nitu', '94556231232');

-- --------------------------------------------------------

--
-- Table structure for table `centredata`
--

CREATE TABLE `centredata` (
  `id` int(11) NOT NULL,
  `centrecode` varchar(20) NOT NULL,
  `centrename` varchar(200) NOT NULL,
  `slots` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `centredata`
--

INSERT INTO `centredata` (`id`, `centrecode`, `centrename`, `slots`) VALUES
(2, '1234', 'Silchar', 9),
(3, '5678', 'Guwahati', 9);

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(1, 'hello '),
(2, 'world');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `adhaar` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `adhaar`, `email`, `dob`) VALUES
(8, '123456789101112', 'akb095@gmail.com', 'pbkdf2:sha256:600000$hDXeGAFAERa5AKy2$3957f522a098fe9be61791959f307ef658e72a3140aa3f48d1a9ac02eae437e8'),
(9, '987654321', 'aryankashyap139@gmail.com', 'pbkdf2:sha256:600000$2wlGTBBUeCn2QeFz$690f18ad7e079444a4f1c67235264e7e14c3663d2fa97fc0b675bf4f258dc084'),
(10, '111222333', 'namitabaishya71@gmail.com', 'pbkdf2:sha256:600000$AAeRLUHUUbqFWDrm$575bb0481176fd0b7a3f237e8ea5f67955424aeb2ae88b677e9782a847909b1d');

-- --------------------------------------------------------

--
-- Table structure for table `vaccinecentres`
--

CREATE TABLE `vaccinecentres` (
  `id` int(11) NOT NULL,
  `centrecode` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vaccinecentres`
--

INSERT INTO `vaccinecentres` (`id`, `centrecode`, `email`, `password`) VALUES
(3, '1234', 'aryankashyap13@gmail.com', 'pbkdf2:sha256:600000$DJR1B2HbQ9hSQwx2$5948734633ba290af5ae50a189ca5cad6d77c1bef36628bd2e5a3939320cc500'),
(4, '5678', 'akb095@gmail.com', 'pbkdf2:sha256:600000$EJNazigNjcvYOS3y$f530c502c223de1277e273cb633a4e728fae9837d3a58d2f9f0fd277a69617e0'),
(5, '890', 'namitabaishya71@gmail.com', 'pbkdf2:sha256:600000$KyVZn9FPqpIVogXP$c7c0341e282c6c3b97436f14d7736cf34a734a2ce38f08dabadf537474ea6839');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookingslot`
--
ALTER TABLE `bookingslot`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `adhaar` (`adhaar`);

--
-- Indexes for table `centredata`
--
ALTER TABLE `centredata`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `centrename` (`centrecode`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `adhaar` (`adhaar`);

--
-- Indexes for table `vaccinecentres`
--
ALTER TABLE `vaccinecentres`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookingslot`
--
ALTER TABLE `bookingslot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `centredata`
--
ALTER TABLE `centredata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `vaccinecentres`
--
ALTER TABLE `vaccinecentres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
