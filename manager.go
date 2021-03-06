package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
	"time"
)

var index int64
var d *bufio.Reader

func init() {
	index = loadIndex()

	file, err := os.Open("dataset.txt")
	if err != nil {
		log.Fatalf("Error opening dataset file: %v\n", err)
	}
	file.Seek(index, os.SEEK_SET)

	reader := bufio.NewReader(file)
	d = reader
}

func main() {
	http.HandleFunc("/job", job)

	log.Println("Starting...")

	go saveIndex()
	log.Fatalln(http.ListenAndServe(":8080", nil))
}

func job(w http.ResponseWriter, r *http.Request) {
	line, err := d.ReadBytes('\n')
	if err != nil {
		log.Fatalf("Error reading line from dataset: %v\n", err)
	}

	fmt.Fprintf(w, string(line))

	index += int64(len(line))
}

func loadIndex() int64 {
	b, err := ioutil.ReadFile("index.txt")
	if err != nil {
		log.Fatalf("Error opening index file: %v\n", err)
	}

	index, err := strconv.ParseInt(string(b[:len(b)-1]), 10, 64)
	if err != nil {
		log.Fatalf("Could not read index file: %v\n", err)
	}

	return index
}

func saveIndex() {
	for {
		time.Sleep(time.Second * 10)

		err := ioutil.WriteFile("index.txt", []byte(strconv.FormatInt(index, 10)+"\n"), os.FileMode(os.O_CREATE))
		if err != nil {
			log.Fatalf("Error writing index file: %v\n", err)
		}
	}
}
