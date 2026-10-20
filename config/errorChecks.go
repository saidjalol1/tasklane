package config



func CheckErrorCodeForLoginPage(errorCode string) string {
	var errorMessage string

    // Map the short URL code to a clean user-facing message
    switch errorCode {
    case "unauthorized":
        errorMessage = "You must be logged in to access that page."
    case "expired":
        errorMessage = "Your session has expired. Please log in again."
    case "invalid_credentials":
        errorMessage = "Incorrect username or password. Please try again."
    default:
        errorMessage = "" // If the code is unknown or empty, show no error message
    }
	return  errorMessage
}