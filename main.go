package main

import "fmt"

func main() {
    name := "John"
    // Go vet issue: Printf format %d expects an integer but name is string
    fmt.Printf("User Name: %d\n", name)
}
