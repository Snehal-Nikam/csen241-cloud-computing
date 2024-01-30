# Use the official Ubuntu image as a parent image
FROM ubuntu:20.04

# Run the command inside your image filesystem
RUN apt update && apt install -y sysbench zip curl nano

COPY script.sh /
RUN ls | tee -a /tmp/output.log
RUN chmod +x script.sh
# RUN zip result_22.zip *.txt | tee -a /tmp/output.log
# RUN curl --upload-file ./result_22.zip https://free.keep.sh
# RUN cat /tmp/output.log
CMD ["bash"]

