let user1 = new User("Paul McCartney", "paul", "1234", 3);
let user2 = new User("George Harrison", "george", "5678", 2);
let user3 = new User("Richard Starkey", "ringo", "8523", 3);
let admin = new SuperUser("John Lennon", "john", "0000", "admin");

user1.show_info();
admin.show_info();

console.log(`Всего обычных пользователей: ${User.count}`);
console.log(`Всего супер-пользователей: ${SuperUser.count}`);

console.log(User.compare(user1, user2));
console.log(User.compare(admin, user3));
console.log(User.compare(user1, user3));

user3.name = "Ringo Star";
user1.password = "Pa$$w0rd";

console.log(user3.name);
console.log(user2.password);
console.log(user2.login);

user2.login = "geo";

console.log(user1.grade);
admin.grade = 10;
