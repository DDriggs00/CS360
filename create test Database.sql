########################################
# CS 360 Game Test DB
# Devin Driggs
########################################
create database Gamedb;
use Gamedb;
########################
# Create Games table
########################
CREATE TABLE Games
(
  Game      varchar(50) NOT NULL ,
  System    varchar(50) ,
  Publisher varchar(50) ,
  Year      int ,
  Price   	int ,
  PRIMARY KEY (Game)
);

#########################
# Create Systems table
#########################
CREATE TABLE Systems
(
  System    varchar(50) NOT NULL,
  Type      varchar(50),
  Creator   varchar(50),
  YearMade  int,
  Price   	int,
  PRIMARY KEY (System)
);
