# threadComm
python comunication thread

-You need PyQt

https://www.riverbankcomputing.com/software/pyqt/download

instance of the queue class

max_data: Number in maximum bytes per transfer

max_buffer: Number in maximum bytes that can contain the buffer, If it exceeds the maximum of bytes in the buffer were removed the data to be at the maximum specified bytes.

Methods of instance

threadComm.set_data

Definition: Sets data

data: establish data buffer

threadComm.wait_data

Definition: Returns data from the buffer with a timeout

num_loop: Number of times the loop is repeated
-returns a list where data [0] if true everything was correct , data [1] function name , data [2] here are data time_wait: Timeout for each turn of the loop

threadComm.get_data

Definition: Returns the data in the buffer -returns a list where data [0] if true everything was correct , data [1] function name , data [2] here are data

-No arguments

threadComm.len_buffer

Definition: Returns the data in the buffer

-No arguments
