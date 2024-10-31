package Collection

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

func GetData() {
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file.")
	}

	Url := os.Getenv("URL")
	ApiKey := os.Getenv("API_KEY")
}
