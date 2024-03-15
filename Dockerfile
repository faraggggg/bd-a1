FROM ubuntu

RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3 \
    python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy
RUN mkdir -p /home/doc-bd-a1/
COPY dod.csv /home/doc-bd-a1/
EXPOSE 8080
CMD ["bash"]
