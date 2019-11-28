import fresh_tomatoes
import movie

the_shining = movie.Movie("The Shining","The central character in The Shining is Jack Torrance (Nicholson), an aspiring writer and recovering alcoholic, who accepts a position as the off-season caretaker of the isolated historic Overlook Hotel in the Colorado Rockies. Wintering over with Jack are his wife Wendy Torrance (Duvall) and young son Danny Torrance (Lloyd). Danny possesses \"the shining\", psychic abilities that enable him to see into the hotel's horrific past. The hotel's cook, Dick Hallorann (Crothers), also has this and is able to telepathically communicate with Danny. The hotel had a previous winter caretaker who went insane and killed his family and himself. After a winter storm leaves the Torrances snowbound, Jack's sanity deteriorates due to the influence of the supernatural forces that inhabit the hotel, placing his wife and son in danger.",
                          "https://upload.wikimedia.org/wikipedia/en/e/ea/The_Shining_%281980%29.png",
                          "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

cars_3 = movie.Movie("Cars 3","Animated film on cars","https://static.posters.cz/image/750webp/64375.webp","https://www.youtube.com/watch?v=2LeOH9AGJQM")

the_conjuring = movie.Movie("The Conjuring","A true story based horror film","https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg","https://www.youtube.com/watch?v=k10ETZ41q5o")

american_pie = movie.Movie("American Pie","A adult comedy film","https://upload.wikimedia.org/wikipedia/en/c/c8/American_Pie1.jpg","https://www.youtube.com/watch?v=Sithad108Og")

peaky_blinders = movie.Movie("Peaky Blinders season 5","History crime drama fiction series","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-RGjQL7pAlGZCk6IQx8UpjqC52SiYTfO0yiGhwvBw4d7m1qdcJg","https://www.youtube.com/watch?v=Ruyl8_PT_y8")

joker = movie.Movie("Joker","An iconic movie","https://preview.redd.it/46glavkeizp21.jpg?width=640&crop=smart&auto=webp&s=aebef49305747d4dcd167ae680c1a8f63ec162cd","https://www.youtube.com/watch?v=zAGVQLHvwOY")

movies = [the_shining,cars_3,the_conjuring,american_pie,peaky_blinders,joker]
fresh_tomatoes.open_movies_page(movies)