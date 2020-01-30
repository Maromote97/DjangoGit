-- phpMyAdmin SQL Dump
-- version 4.0.10.14
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Czas wygenerowania: 30 Sty 2020, 08:28
-- Wersja serwera: 5.0.95
-- Wersja PHP: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Baza danych: `s145867`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Klient`
--

CREATE TABLE IF NOT EXISTS `Klient` (
  `Pesel` int(11) NOT NULL,
  `Imie` varchar(45) NOT NULL,
  `Nazwisko` varchar(45) NOT NULL,
  `Miejscowosc` varchar(45) NOT NULL,
  PRIMARY KEY  (`Pesel`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `Klient`
--

INSERT INTO `Klient` (`Pesel`, `Imie`, `Nazwisko`, `Miejscowosc`) VALUES
(2147483647, 'Mariusz', 'Makowski', 'Olsztyn');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Ksiazka`
--

CREATE TABLE IF NOT EXISTS `Ksiazka` (
  `Id_Ksiazki` int(13) NOT NULL,
  `Autor` varchar(45) NOT NULL,
  `Tytul` varchar(45) NOT NULL,
  `Dostepnosc` int(13) NOT NULL,
  `Cena_za_miesiac` float NOT NULL,
  PRIMARY KEY  (`Id_Ksiazki`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `Ksiazka`
--

INSERT INTO `Ksiazka` (`Id_Ksiazki`, `Autor`, `Tytul`, `Dostepnosc`, `Cena_za_miesiac`) VALUES
(123, 'George Orwell', 'Folwark Zwierzecy', 7, 3),
(124, 'George Orwell', 'Rok 1984', 5, 3.5),
(125, 'J. K. Rowling', 'Harry Potter i Kamie? Filozoficzny', 4, 2.8),
(126, 'J. K. Rowling', 'HK Kamien Filozoficzny', 3, 2.8),
(127, 'J. K. Rowling', 'HK Komnata Tajemnic', 6, 3.3),
(128, 'J. K. Rowling', 'HK Wiezien azkabanu', 9, 2.5),
(129, 'Dmitry Glukhovsky', 'Metro 2033', 1, 5),
(130, 'Dmitry Glukhovsky', 'Metro 2033', 2, 4.5);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Pracownik`
--

CREATE TABLE IF NOT EXISTS `Pracownik` (
  `Id_Pracownik` int(11) NOT NULL,
  `Imie` varchar(45) NOT NULL,
  `Nazwisko` varchar(45) NOT NULL,
  `Stanowisko` varchar(45) NOT NULL,
  PRIMARY KEY  (`Id_Pracownik`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `Pracownik`
--

INSERT INTO `Pracownik` (`Id_Pracownik`, `Imie`, `Nazwisko`, `Stanowisko`) VALUES
(111, 'Tadeusz', 'Piatek', 'Kasjer'),
(11, 'Miroslaw', 'Pogoda', 'Bibliotekarz');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Wypozyczanie`
--

CREATE TABLE IF NOT EXISTS `Wypozyczanie` (
  `IdWypozyczenia` int(13) NOT NULL,
  `Klient_Pesel` int(11) NOT NULL,
  `Id_Ksiazki` int(13) NOT NULL,
  `Pracownik_IdPracownik` int(13) NOT NULL,
  `Data_wydania` date NOT NULL,
  `Data_oddania` date NOT NULL,
  `Cena_za_wypozyczenie` float NOT NULL,
  PRIMARY KEY  (`IdWypozyczenia`),
  KEY `Id_Ksiazki` (`Id_Ksiazki`),
  KEY `Klient_Pesel` (`Klient_Pesel`),
  KEY `Pracownik_IdPracownik` (`Pracownik_IdPracownik`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `Wypozyczanie`
--

INSERT INTO `Wypozyczanie` (`IdWypozyczenia`, `Klient_Pesel`, `Id_Ksiazki`, `Pracownik_IdPracownik`, `Data_wydania`, `Data_oddania`, `Cena_za_wypozyczenie`) VALUES
(1, 2147483647, 126, 11, '2019-12-11', '2020-01-14', 2.8);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
