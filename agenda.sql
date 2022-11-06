-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2022 a las 15:23:20
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `idArea` int(200) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`idArea`, `nombre`) VALUES
(1, 'Limpieza'),
(2, 'Finanzas'),
(3, 'mantenimiento de computo'),
(4, 'Recursos Humanos'),
(5, 'Contabilidad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `idCarrera` int(200) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`idCarrera`, `nombre`) VALUES
(1, 'programacion'),
(2, 'enfermeria'),
(3, 'contabilidad'),
(4, 'mantenimiento'),
(5, 'Arquitectura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escolaridad`
--

CREATE TABLE `escolaridad` (
  `idEscolaridad` int(200) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `escolaridad`
--

INSERT INTO `escolaridad` (`idEscolaridad`, `nombre`) VALUES
(1, 'Secundaria'),
(2, 'Primaria'),
(3, 'Preparatoria'),
(4, 'Preparatoria Trunca'),
(5, 'Ninguna');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadocivil`
--

CREATE TABLE `estadocivil` (
  `idEstadocivil` int(5) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadocivil`
--

INSERT INTO `estadocivil` (`idEstadocivil`, `nombre`) VALUES
(1, 'Solter@'),
(2, 'Casad@'),
(3, 'Union libre'),
(4, 'Viud@'),
(5, 'Divorciad@');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grado_avance`
--

CREATE TABLE `grado_avance` (
  `idGradoAvance` int(200) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `grado_avance`
--

INSERT INTO `grado_avance` (`idGradoAvance`, `nombre`) VALUES
(1, 'mal'),
(3, 'bueno'),
(4, 'Excelente'),
(6, 'bastante malo'),
(7, 'pasable');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad`
--

CREATE TABLE `habilidad` (
  `idHabilidad` int(200) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `habilidad`
--

INSERT INTO `habilidad` (`idHabilidad`, `nombre`) VALUES
(1, 'Jugar'),
(2, 'Barrer'),
(3, 'Contar'),
(4, 'Arreglar laps'),
(5, 'Leer fluido');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idioma`
--

CREATE TABLE `idioma` (
  `idIdioma` int(200) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `idioma`
--

INSERT INTO `idioma` (`idIdioma`, `nombre`) VALUES
(1, 'Español'),
(2, 'Aleman'),
(3, 'Portugues'),
(4, 'Frances'),
(5, 'Ingles');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mediopublic`
--

CREATE TABLE `mediopublic` (
  `idMedioPublic` int(200) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `mediopublic`
--

INSERT INTO `mediopublic` (`idMedioPublic`, `nombre`) VALUES
(1, 'Television '),
(2, 'Periodico'),
(3, 'Redes Sociales'),
(4, 'Radio'),
(5, 'Cartel');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `codPuesto`, `idArea`, `nomPuesto`, `puestoJefeSup`, `jornada`, `remunMensual`, `prestaciones`, `descripcionGeneral`, `funciones`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `experiencia`, `conocimientos`, `manejoEquipo`, `reqFisicos`, `reqPsicologicos`, `responsabilidades`, `condicionesTrabajo`) VALUES
(17, '0710', 3, 'reparador', 'Reparador de software', 'De lunes a Viernes', 15000, 'De ley', 'Reparar computadoras y darles su mantenimiento semanal', 'no se', '24', 'Hombre', 1, 3, 7, 1, '13 años', 'Reparacion completa de una pc o lap', 'Todo tipo de herramientas', 'Ninguno', 'Saludable', 'Ninguna', 'Buenas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_habilidad`
--

CREATE TABLE `puesto_has_habilidad` (
  `idpuesto` int(11) NOT NULL,
  `idHabilidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puesto_has_habilidad`
--

INSERT INTO `puesto_has_habilidad` (`idpuesto`, `idHabilidad`) VALUES
(17, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_idioma`
--

CREATE TABLE `puesto_has_idioma` (
  `idpuesto` int(11) NOT NULL,
  `ididioma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puesto_has_idioma`
--

INSERT INTO `puesto_has_idioma` (`idpuesto`, `ididioma`) VALUES
(17, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `requisicion`
--

CREATE TABLE `requisicion` (
  `idRequisicion` int(11) NOT NULL,
  `folio` varchar(25) NOT NULL,
  `fechaElab` date NOT NULL,
  `fechaRecluta` date NOT NULL,
  `fechaInicVac` date NOT NULL,
  `motivoRequisicion` varchar(30) NOT NULL,
  `motivoEspecifique` varchar(70) NOT NULL,
  `tipoVacante` varchar(15) NOT NULL,
  `nomSolicita` varchar(70) NOT NULL,
  `nomAutoriza` varchar(70) NOT NULL,
  `nomRevisa` varchar(70) NOT NULL,
  `autorizada` tinyint(1) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `idArea` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `requisicion`
--

INSERT INTO `requisicion` (`idRequisicion`, `folio`, `fechaElab`, `fechaRecluta`, `fechaInicVac`, `motivoRequisicion`, `motivoEspecifique`, `tipoVacante`, `nomSolicita`, `nomAutoriza`, `nomRevisa`, `autorizada`, `idPuesto`, `idArea`) VALUES
(17, '001', '2022-10-24', '2022-10-24', '2022-10-25', 'Nueva Creación', '', 'Libre', 'Ian Aaron Valencia Martinez Reparado de computo', 'Viviana de recursos humanos', 'Viviana de recursos humanos', 1, 17, 3),
(23, '002', '2022-10-24', '2022-10-21', '2022-10-09', 'Nueva Creación', '', 'ASDASDAS', 'qs', '', '', 0, 17, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`idCarrera`);

--
-- Indices de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  ADD PRIMARY KEY (`idEscolaridad`);

--
-- Indices de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  ADD PRIMARY KEY (`idEstadocivil`);

--
-- Indices de la tabla `grado_avance`
--
ALTER TABLE `grado_avance`
  ADD PRIMARY KEY (`idGradoAvance`);

--
-- Indices de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  ADD PRIMARY KEY (`idHabilidad`);

--
-- Indices de la tabla `idioma`
--
ALTER TABLE `idioma`
  ADD PRIMARY KEY (`idIdioma`);

--
-- Indices de la tabla `mediopublic`
--
ALTER TABLE `mediopublic`
  ADD PRIMARY KEY (`idMedioPublic`);

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`),
  ADD KEY `idEscolaridad` (`idEscolaridad`),
  ADD KEY `idEstadoCivil` (`idEstadoCivil`),
  ADD KEY `idGradoAvance` (`idGradoAvance`),
  ADD KEY `idCarrera` (`idCarrera`),
  ADD KEY `area` (`idArea`);

--
-- Indices de la tabla `puesto_has_habilidad`
--
ALTER TABLE `puesto_has_habilidad`
  ADD PRIMARY KEY (`idpuesto`,`idHabilidad`),
  ADD KEY `idhabilidad` (`idHabilidad`);

--
-- Indices de la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  ADD PRIMARY KEY (`idpuesto`,`ididioma`),
  ADD KEY `ididioma` (`ididioma`);

--
-- Indices de la tabla `requisicion`
--
ALTER TABLE `requisicion`
  ADD PRIMARY KEY (`idRequisicion`),
  ADD KEY `idPuesto` (`idPuesto`),
  ADD KEY `idArea` (`idArea`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `area`
--
ALTER TABLE `area`
  MODIFY `idArea` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `idCarrera` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  MODIFY `idEscolaridad` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  MODIFY `idEstadocivil` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `grado_avance`
--
ALTER TABLE `grado_avance`
  MODIFY `idGradoAvance` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  MODIFY `idHabilidad` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `idioma`
--
ALTER TABLE `idioma`
  MODIFY `idIdioma` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `mediopublic`
--
ALTER TABLE `mediopublic`
  MODIFY `idMedioPublic` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `requisicion`
--
ALTER TABLE `requisicion`
  MODIFY `idRequisicion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `puesto_has_habilidad`
--
ALTER TABLE `puesto_has_habilidad`
  ADD CONSTRAINT `relaciondosh` FOREIGN KEY (`idHabilidad`) REFERENCES `habilidad` (`idHabilidad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `relacionunoh` FOREIGN KEY (`idpuesto`) REFERENCES `puesto` (`idPuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  ADD CONSTRAINT `relaciondos` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`idIdioma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `relacionuno` FOREIGN KEY (`idpuesto`) REFERENCES `puesto` (`idPuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
