# threadComm

python comunication thread

Requisites
You need PyQt

https://www.riverbankcomputing.com/software/pyqt/download

instance of the queue class
---
* params instance
  *`max_data`(int )Number in maximum bytes per transfer
  * `max_buffer`: Number in maximum bytes that can contain the buffer, If it exceeds the maximum of bytes in the buffer were removed the data to be at the maximum specified bytes.
 
* `set_data`(anyone data):Sets data
  * `data` establish data buffer

* `wait_data` Returns data from the buffer with a timeout

* `num_loop` Number of times the loop is repeated.Returns a list where data [0] if true everything was correct , data [1] function name , data [2] here are data time_wait: Timeout for each turn of the loop.

* `get_data` Returns the data in the buffer -returns a list where data [0] if true everything was correct , data [1] function name , data [2] here are data.

* `buffer`eturns the data in the buffer
---
