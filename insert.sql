INSERT INTO Genres (genreid, genre_name)
VALUES
	(11,'pop'),
	(12,'rap'),
	(13,'chanson'),
	(14,'rock'),
	(15,'classic');

INSERT INTO Artists (artistid, "name")
values 
	(21,'Адель'),
	(22,'Джастин Бибер'),
	(23,'Miyagi'),
	(24,'Джастин Тимберлейк'),
	(25,'Katy Perri'),
	(26,'Майкл Джексон'),
	(27,'The Beatles'),
	(28,'Шарль Азнавур'),
	(29,'Ludovico Einaudi');

INSERT INTO Albums (albumid, album_name, release_year)
values 
	(31,'30', 2020),
	(32,'Justice', 2020),
	(33,'Captain', 2018),
	(34,'Justified', 2002),
	(35,'One of the Boys', 2012),
	(36,'Thriller', 1982),
	(37,'Abbey Road', 1969),
	(38,'20 Chansons Dor', 1987),
	(39,'Una Mattina', 2004);

alter table tracks
drop column TIME;

alter table tracks
ADD column time numeric(3,2) not null;

alter table tracks 
add column albumID integer;

alter table tracks
ADD CONSTRAINT FK_TracksAlbums
foreign key (trackID) references Albums(albumID);

alter table tracks
drop constraint FK_TracksAlbums;

alter table tracks
add constraint FK_TracksAlbums
foreign key (albumID) references Albums(albumID);

alter table tracks
drop constraint tracks_trackid_fkey;

INSERT INTO tracks (trackid, title, time, albumID)
values
	(41,'Easy on Me', 3.2, 31),
	(42,'Deserve You', 3.4, 32),
	(43,'Captain', 3.5, 33),
	(44,'Like I Love You', 4.6, 34),
	(45,'I Kissed a Girl', 3.6, 35),
	(46,'Billie Jean', 3.4, 36),
	(47,'Sun King = Rey Sol', 2.5, 37),
	(48,'La boh?me', 3.7, 38),
	(49,'Nuvole Bianche', 5.5, 39),
	(410,'Thriller', 5.4, 36),
	(411,'Something = Algo', 3.4, 35),
	(412,'La Mamma', 3.6, 38),
	(413,'Ancora', 5.2, 37),
	(414,'I got love', 4.0, 33),
	(415,'По уши я в тебя влюблен', 3.2, 33);

INSERT INTO collections (collectionid, collection_name, release_year)
values
	(51, 'collection_1', 2020),
	(52, 'collection_2', 2020),
	(53, 'collection_3', 2018),
	(54, 'collection_4', 2002),
	(55, 'collection_5', 2012),
	(56, 'collection_6', 1982),
	(57, 'collection_7', 1969),
	(58, 'collection_8', 1987),
	(59, 'collection_9', 2004);

INSERT INTO artists_genres (id,genreid, artistid)
values
	(121,21, 11),
	(122,22, 12),
	(123,23, 12),
	(124,24, 11),
	(125,25, 11),
	(126,26, 11),
	(127,27, 14),
	(128,28, 13),
	(129,29, 15);

INSERT INTO artists_albums (id, artistid, albumid)
values
	(121,31, 21),
	(122,32, 22),
	(123,33, 23),
	(124,34, 24),
	(125,35, 25),
	(126,36, 26),
	(127,37, 27),
	(128,38, 28),
	(129,39, 29);

INSERT INTO tracks_collections (id, collectionid, trackid)
values
	(121,41, 51),
	(122,42, 52),
	(123,43, 53),
	(124,44, 54),
	(125,45, 55),
	(126,46, 56),
	(127,47, 57),
	(128,48, 58),
	(129,49, 59),
	(130,410, 54),
	(131,411, 55),
	(132,412, 56),
	(133,413, 57),
	(134,414, 58),
	(135,415, 59);

INSERT INTO tracks_collections (id, collectionid, trackid)
values
	(136,415, 58);

INSERT INTO artists_genres (id,genreid, artistid)
values
	(130,28, 14);

INSERT INTO tracks (trackid, title, time, albumID)
values
	(416,'Колибри', 3.4, 33);
