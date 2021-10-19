create table Artist (
 id	        integer primary key autoincrement,
 artistname 	varchar(64) not null,
 hometown 	varchar(64) not null,
 description varchar(128) not null
);

create table Event (
  id		      integer primary key autoincrement,
  eventname 	varchar(64) not null,
  date 	DATETIME not null
);

create table Venue (
  id	          integer primary key autoincrement,
  venuename  varchar(64) not null,
  eventID integer not null,
  foreign key (eventID) references Event(id)
);

create table ArtistToEvent (
  id	      integer primary key autoincrement,
  artistID integer not null,
  eventID integer not null,
  foreign key (artistID) references Artist(id),
  foreign key (eventID) references Event(id)
);



