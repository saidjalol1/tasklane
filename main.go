package main

import (
	"tasklane/config"
	"tasklane/routers"
	
	
	"log"
	"github.com/gin-gonic/gin"

)

func main(){

	
	server := gin.Default()
	server.LoadHTMLGlob(config.TEMPLATES_DIR)
	server.Static(config.STATIC_FILES_URL, config.STATIC_FILES_DIRS)


	// Routers 
	server.GET("/", routers.Home)
	server.GET("/profile", routers.ProfilePage)
	server.GET("/manage", routers.ManagePage)


	authRoutes := server.Group("auth/")
	authRoutes.GET("/login", routers.LoginPage)
	authRoutes.GET("/register", routers.RegisterPage)


	log.Printf("[ INFO ] Starting the server at %s", config.GIN_PORT)
	if err := server.Run(config.GIN_PORT); err != nil {
		log.Fatalf("[ ERROR ] Failed to start the server: %v", err)
	}

}