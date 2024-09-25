## DOCKER
### 1. What is Docker
Nền tảng phần mềm cho phép xây dựng, kiểm thử triển khai ứng dụng trong package virtual containerized enviroment. Docker cho phép apps hoạt động bình thường ở mọi nơi, dù trên bất cứ OS nào.
+ **Docker File**: Design cho Docker Image. File không có phần mở rộng (đuôi file).
+ **Docker Image**: chỉ tồn tại ở dạng read-only chứa cách để tạo ra các container. Là snapshot hoặc blueprint của libraries và dependances cần có trong container nhằm phục vụ cho application.
+ **Docker container**:
  - Môi trường cách li để chạy ứng dụng. Deloy trên bất cứ machine nào mà không gặp compatibility issue. Giúp software bảo toàn tính nguyên vẹn hệ thống, dễ dàng sử dụng, đơn giản hơn khi develop, dễ dàng bảo trì và deploy.
  - Mỗi Container hoạt động như một micro PC, với OS và CPU độc lập, memory, Network resources => add/remove/stop/restart mà không ảnh hưởng các container khác hay host machine.
  - Mỗi Container thường chạy một specific task sau đó được nối vào network
Khác với Virtual machines, resource được chia sẽ trực tiếp với host => cho phép chạy nhiều Docker Container.
Docker ít tốn dung lượng ổ cứng do tái sử dụng file bằng layered file system. Nếu có nhiều Docker image cùng sử dụng một base image một lúc, Docker sẽ chỉ giữ lại một bản copy của files cần thiết và chia sẽ chúng với các container.
### 2.Why do we need Docker
+ **Compatibility**:
  - **Different programming languages** có thể không cùng có libraries => xung đột chương trình.
  - **Different library versions** => code hoạt động với version này nhưng không hoạt động với version mới hơn.
  - **OS**: Ứng dụng có thể chạy trên OS A nhưng chưa chắc đã có thể chạy trên các OS khác.
+ Triển khai ứng dụng trên **Remote servers**: Container chứa code, libraries, data.
### 3. How to use Docker
+ **Docker File**:
  - Tạo base image bắt đầu với từ khóa `FROM` (có thể lấy build sẵn từ Dockerhub), lựa chọn phổ biến là Ubuntu và Alpine Linux.
  - `WORKDIR` (optional): làm việc ở folder nào.
  - `COPY`: copy files từ máy vào Docker image.
  - Sau đó có thể `RUN` commands (khởi tạo môi trường, cài đặt các thư viện,...)
  - `EXPOSE` (for web dev và docker compose): mở port. Cho phép truy cập từ máy khi lauch web trong Docker container.
  - `CMD` (only): xác định command muốn chạy khi chạy Docker container.
+ **Docker Image**:
  - Build Docker file: `docker build -t filename .`
  - Run Docker Image: `docker run image_name`
  - Run Docker Image ở dạng interactive: `docker run -it image_name bash`
**Note:** Có thể tạo ra nhiều Docker Container chạy độc lập trên cùng 1 một thiết bị phần cứng.
**_Dockerfile =build=> Docker Image =run=> Docker Container_**

## DOCKER COMPOSE
### 1. What is Docker Compose
- Docker Compose là công cụ để định nghĩa và chạy multi-container cho Docker applications. Compose sử dụng file YAML để config các service cho applications. Sau đó dùng command để create và run từ các config đó. Với 3 bước:
  - Khai báo app’s enviroment
  - Khai báo services cần thiết để chạy applications trong file docker-compose.yml
  - Run docker-compose up để start và run app
### 2. Why do we use Docker Compose
 - **Simplified control**: Docker compose cho phép định nghĩa và quản lí multi-container trong một file YAML. Giúp dễ dàng replicate appliction enviroment.
 - **Efficient collaboration**:  Docker compose configuration files dễ chia sẽ giữa developers, ops team, và stakeholders.
 - **Rapid application development**: Compose catches configurations được dùng để tạo ra container. Nếu restart một service cũ, Compose sẽ tái sử dụng lại các containers đã tồn tại.
 - **Portability across enviroment**: Compose supports variable trong Compose files. Ta có thể dùng variables này để customize composition for các môi trường/user khác nhau.
### 3. Use cases
 - **Development enviroment**: Compose file cung cấp cách để document và configure tất cả application’s service dependencies (database, queues, catches, web services API). Bằng việc sử dụng Compose Command line tool ta có thể create và start một hoặc nhiều containers cho mỗi dependencies với 1 dòng lệnh (docker compose up).
 - **Automated testing enviroment**: Với Compose ta có thể create and destroy các testing enviroment độc lập cho test suit, tự động hóa end-to-end testsuit.
 - **Single host deployment**.