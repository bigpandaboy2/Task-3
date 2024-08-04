class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.movie_counter = 1
        self.user_counter = 1
        self.ticket_counter = 1

    def addMovie(self, movieName):
        movie_id = self.movie_counter
        self.movies[movie_id] = movieName
        self.movie_counter += 1
        return movie_id

    def showAllMovies(self):
        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def addUser(self, userName):
        user_id = self.user_counter
        self.users[user_id] = userName
        self.user_counter += 1
        return user_id

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticket_id = self.ticket_counter
            self.tickets[ticket_id] = (userId, movieId)
            self.ticket_counter += 1
            return ticket_id
        return None

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        return False

def main():
    cinemaSystem = CinemaTicketSystem()
    while True:
        print("Здравствуйте, у вас есть следующие доступные функции:")
        print("1. Добавить новый фильм")
        print("2. Показать все доступные фильмы")
        print("3. Добавить нового пользователя")
        print("4. Купить билет")
        print("5. Отменить покупку билета")
        print("0. Выход")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            movie_name = input("Введите название фильма: ")
            movie_id = cinemaSystem.addMovie(movie_name)
            print(f"Фильм добавлен с идентификатором {movie_id}.")
        
        elif choice == "2":
            cinemaSystem.showAllMovies()
        
        elif choice == "3":
            user_name = input("Введите имя пользователя: ")
            user_id = cinemaSystem.addUser(user_name)
            print(f"Пользователь добавлен с идентификатором {user_id}.")
        
        elif choice == "4":
            user_id = int(input("Введите идентификатор пользователя: "))
            movie_id = int(input("Введите идентификатор фильма: "))
            ticket_id = cinemaSystem.buyTicket(user_id, movie_id)
            if ticket_id:
                print(f"Билет куплен с идентификатором {ticket_id}.")
            else:
                print("Ошибка при покупке билета.")
        
        elif choice == "5":
            ticket_id = int(input("Введите идентификатор билета: "))
            if cinemaSystem.cancelTicket(ticket_id):
                print("Билет успешно отменен.")
            else:
                print("Билет с таким идентификатором не найден.")
        
        elif choice == "0":
            print("Выход.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
