package routers

import (
	"fmt"
	"net/http"

	"tasklane/config"

	"github.com/gin-gonic/gin"
)


func Home(context *gin.Context){
	config.Render(context, http.StatusOK, "index.html", gin.H{
		"title":"Tasklane · Home",
	})
}


func ManagePage(context *gin.Context) {
	config.Render(context, http.StatusOK, "manage.html", gin.H{
		"title":"Tasklane · Manage Your Tasks",
	})
}


func LoginPage(context *gin.Context) {
	errorCode := context.Query("error")
	errorMessage := config.CheckErrorCodeForLoginPage(errorCode)
	
	config.Render(context, http.StatusOK, "login.html", gin.H{
		"title":"Tasklane · Login",
		"message":errorMessage,
	})
}


func RegisterPage(context *gin.Context) {
	config.Render(context, http.StatusOK, "register.html", gin.H{
		"title":"Tasklane · Register Page",
	})
}


func ProfilePage(context *gin.Context) {

	userProfileData, exists  := context.Get("user")
	if !exists {
		context.Redirect(http.StatusFound, "/auth/login?error=unauthorized")
		return
	}

	userData := userProfileData.(config.User)

	config.Render(context, http.StatusOK, "profile.html", gin.H{
		"title":fmt.Sprintf("Tasklane · %s", userData.Username),
		"user": userData,
	})
}