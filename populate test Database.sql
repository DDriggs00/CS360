########################################
# Populate script Project Sample Database
# Devin Driggs
########################################

USE Gamedb;

########################
# Populate Games table
########################
INSERT INTO Games(Game, System, Publisher, Year, Price)
VALUES('Sonic', 'Sega Genesis', 'SEGA', 1991, 20),
	    ('Super Mario', 'NES', 'Nintendo', 1985, 10),
	    ('Mario Kart 7', '3DS', 'Nintendo', 2011, 40),
	    ('Undertale', 'PC', 'Toby Fox', 2015, 15),
	    ('Minecraft', 'PC', 'Mojang', 2009, 30),
	    ('Pokemon Emerald', 'GBA', 'Game Freak', 2004, 20),
	    ('Pokemon Heart Gold', 'DS', 'Game Freak', 2009, 45),
	    ('Pokemon Sun', '3DS', 'Game Freak', 2016, 50),
      ('Divinity Original Sin', 'PC', 'Larian Studios', 2014, 45),
			('Divinity Original Sin 2', 'PC', 'Larian Studios', 2017, 60);

#########################
# Populate Systems table
#########################
INSERT INTO Systems(System, Type, Creator, YearMade)
VALUES('NES', 'Console', 'Nintendo', 1985, 50),
			('Sega Genesis', 'Console', 'SEGA', 1991, 30),
			('3DS', 'Handheld', 'Nintendo', 2011, 200),
			('DS', 'Handheld', 'Nintendo', 2004, 100),
			('GBA', 'Handheld', 'Nintendo', 2001, 70),
      ('PC', 'Console', 'Microsoft', 1985, 600);
