-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 31 Tem 2024, 18:28:43
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `inf`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `car_park`
--

CREATE TABLE `car_park` (
  `car_id` int(11) NOT NULL,
  `driver_name_surname` varchar(200) NOT NULL,
  `car_plate` varchar(100) NOT NULL,
  `car_brand` varchar(200) NOT NULL,
  `car_model` varchar(100) NOT NULL,
  `driver_sex` varchar(100) NOT NULL,
  `driver_age` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `car_park`
--

INSERT INTO `car_park` (`car_id`, `driver_name_surname`, `car_plate`, `car_brand`, `car_model`, `driver_sex`, `driver_age`) VALUES
(37, 'TALHA KILIÇ', '34 DOU 97', 'VOLVO', 'S90', 'ERKEK', 26),
(40, 'TAYFUN SOY ', '34 TYF 34', 'PORCHE', 'SPIDER', 'ERKEK', 32),
(42, 'KADİR SANCAR', '34 KDR 23', 'VOLKSWAGEN', 'GOLF', 'ERKEK', 20),
(44, 'EMRE GÜNEY ', '34 FEV 433', 'HYUNDAİ', 'BYON', 'ERKEK', 23),
(45, 'ZEHRA KILIÇ', '34 ZHR 58', 'MERCEDES', 'VITO', 'KADIN', 53),
(47, 'YAKUP BATO', '34 BT 5757', 'MASERATI', 'LEVANTE', 'ERKEK', 25),
(49, 'TALHA KILIÇ', '34 FB 1907', 'MERCEDES', 'S360', 'ERKEK', 26),
(50, 'AHMET ERCANLAR', '34 AHM 1907', 'MERCEDES ', 'TOROS', 'ERKEK', 45),
(54, 'KADİR AYDEMİR', '34 FSM 414', 'PEUGEOT', '3008', 'ERKEK', 34),
(55, 'YAĞIZ SABUN', '34 DOU 34', 'BENTLEY', 'CONTİNENTAL GT', 'ERKEK', 34),
(56, 'YAKUP BATO', '56 BAT 907', 'MASERATI', 'LEVANTE', 'ERKEK', 25),
(57, 'GİRAY ESEN', '34 LAZ 53', 'TOROS', 'TOROS', 'ERKEK', 90),
(58, 'ZEHRA KILIÇ', '34 SVS 58', 'PEUGEOT', '3008', 'KADIN', 53);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'Talha ', '1234'),
(3, 'TLH', '123'),
(5, 'UFB', '123'),
(6, 'DOUFB', '123'),
(9, 'T', '1'),
(10, 'A', '1'),
(11, '', ''),
(12, 'EMRE', '12345'),
(13, 'EMR', '1');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `car_park`
--
ALTER TABLE `car_park`
  ADD PRIMARY KEY (`car_id`);

--
-- Tablo için indeksler `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `car_park`
--
ALTER TABLE `car_park`
  MODIFY `car_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- Tablo için AUTO_INCREMENT değeri `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
