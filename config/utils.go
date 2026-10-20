package config 

import (
    "github.com/gin-gonic/gin"
)

// Render automatically injects global URLs and common data into every template
func Render(c *gin.Context, status int, templateName string, data gin.H) {
    // If custom data wasn't passed, initialize an empty map
    if data == nil {
        data = gin.H{}
    }

    data["Urls"] = URLS
	data["Path"] = c.FullPath()

    // Render the actual Gin HTML template
    c.HTML(status, templateName, data)
}