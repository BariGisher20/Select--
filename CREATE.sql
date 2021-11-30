create table if not exists Genres (
	genreID integer primary key,
	genre_name text not null
);

create table if not exists Artists (
	artistID integer primary key,
	name text not null
);

create table if not exists Artists_Genres (
	ID integer primary key,
	artistID integer not null,
	genreID integer not null,
	foreign key (artistID) references Genres(genreID),
	foreign key (genreID) references Artists(artistID)
);

create table if not exists Albums (
	albumID integer primary key,
	album_name text not null,
	release_year integer not null
);

create table if not exists Artists_Albums (
	ID integer primary key,
	artistID integer not null,
	albumID integer not null,
	foreign key (artistID) references Albums(albumID),
	foreign key (albumID) references Artists(artistID)
);

create table if not exists Tracks (
	trackID integer primary key,
	title text not null,
	time numeric not null,
	foreign key (trackID) references Albums(albumID)
);

create table if not exists Collections (
	collectionID integer primary key,
	collection_name text not null,
	release_year integer not null
);

create table if not exists Tracks_Collections (
	ID integer primary key,
	collectionID integer not null,
	trackID integer not null,
	foreign key (collectionID) references Tracks(trackID),
	foreign key (trackID) references Collections(collectionID)
);





