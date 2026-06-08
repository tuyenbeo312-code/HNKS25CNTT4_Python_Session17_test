students_list = [
    {
        "student_id": "SV001",
        "student_name": "Nguyen Van A",
        "math_score": 8.5,
        "physics_score": 7.0,
        "chemistry_score": 9.0,
        "avg_score": 8.17,
        "rank": "Giỏi",
    },
    {
        "student_id": "SV002",
        "student_name": "Nguyen Van B",
        "math_score": 8.0,
        "physics_score": 7.6,
        "chemistry_score": 9.0,
        "avg_score": 8.2,
        "rank": "Giỏi",
    },
]


def display_students(list):
    if len(list) == 0:
        print("Danh sách sinh viên trống!")
        return
    print("----------- Danh sách sinh viên -----------")
    print(
        f"{'Mã sinh viên'} | {'Tên sinh viên'} | {'Điểm Toán'} | {'Điểm Lý'} | {'Điểm Hóa'} | {'Điểm Trung Bình'} | {'Xếp loại'}"
    )
    print("=" * 90)
    for student in list:
        print(
            "{student_id:<12} | {student_name:<13} | {math_score:<9} | {physics_score:<7} | {chemistry_score:<8} | {avg_score:<15} | {rank}".format_map(
                student
            )
        )
    print("=" * 90)


def check_rank(avg_score):
    if 8.0 <= avg_score <= 10.0:
        return "Giỏi"
    elif 7.0 <= avg_score < 8.0:
        return "Khá"
    elif 5.0 <= avg_score < 7.0:
        return "Trung Bình"
    else:
        return "Yếu"


def add_student(list):
    while True:
        add_student_id = input("Nhập vào mã sinh viên muốn thêm: ").strip().upper()
        if add_student_id == "":
            print("Mã sinh viên không được để trống")
            continue
        found = False
        for student in list:
            if student["student_id"] == add_student_id:
                print("Lỗi ! mã sinh viên đã tồn tại!")
                found = True
                break
        if not found:
            break
    while True:
        add_student_name = input("Nhập tên sinh viên muốn thêm: ").strip().title()
        if add_student_name == "":
            print("Lỗi ! tên sinh viên không được để trống!")
            continue
        else:
            break
    while True:
        try:
            math_score = float(input("Nhập điểm toán cho sinh viên muốn thêm: "))
            if not (0 <= math_score <= 10):
                print("Lỗi điểm toán phải nằm trong khoảng 0 - 10")
                continue
        except:
            print("Lỗi! điểm toán không hợp lệ!")
            continue
        else:
            break

    while True:
        try:
            physics_score = float(input("Nhập điểm lý cho sinh viên muốn thêm: "))
            if not (0 <= physics_score <= 10):
                print("Lỗi điểm lý phải nằm trong khoảng 0 - 10")
                continue
        except:
            print("Lỗi! điểm lý không hợp lệ!")
            continue
        else:
            break
    while True:
        try:
            chemistry_score = float(input("Nhập điểm hóa cho sinh viên muốn thêm: "))
            if not (0 <= chemistry_score <= 10):
                print("Lỗi điểm hóa phải nằm trong khoảng 0 - 10")
                continue
        except:
            print("Lỗi! điểm hóa không hợp lệ!")
            continue
        else:
            break

    avg_score = float((math_score + physics_score + chemistry_score) / 3)

    rank = check_rank(avg_score)

    new_student = {
        "student_id": add_student_id,
        "student_name": add_student_name,
        "math_score": math_score,
        "physics_score": physics_score,
        "chemistry_score": chemistry_score,
        "avg_score": avg_score,
        "rank": rank,
    }
    list.append(new_student)
    print(f"Thêm sinh viên {new_student['student_name']} thành công")


def update_student_score(list):
    while True:
        update_student_id = (
            input("Nhập vào mã sinh viên muốn cập nhật: ").strip().upper()
        )
        if update_student_id == "":
            print("Mã sinh viên không được để trống")
            continue
        found = False
        for student in list:
            if student["student_id"] == update_student_id:
                found = True
                print("============= Thông tin sinh viên =============")
                print("=" * 90)
                print(
                    "{student_id:<12} | {student_name:<13} | {math_score:<9} | {physics_score:<7} | {chemistry_score:<8} | {avg_score:<15} | {rank}".format_map(
                        student
                    )
                )
                print("=" * 90)
                break
        if not found:
            print("Lỗi! không tìm thấy sinh viên")
            continue
        else:
            break
    while True:
        try:
            math_score = float(input("Nhập điểm toán cho sinh viên: "))
            if not (0 <= math_score <= 10):
                print("Lỗi điểm toán phải nằm trong khoảng 0 - 10")
                continue
        except:
            print("Lỗi! điểm toán không hợp lệ!")
            continue
        else:
            break

    while True:
        try:
            physics_score = float(input("Nhập điểm lý cho sinh viên: "))
            if not (0 <= physics_score <= 10):
                print("Lỗi điểm lý phải nằm trong khoảng 0 - 10")
                continue
        except:
            print("Lỗi! điểm lý không hợp lệ!")
            continue
        else:
            break
    while True:
        try:
            chemistry_score = float(input("Nhập điểm hóa cho sinh viên: "))
            if not (0 <= chemistry_score <= 10):
                print("Lỗi điểm hóa phải nằm trong khoảng 0 - 10")
                continue
        except:
            print("Lỗi! điểm hóa không hợp lệ!")
            continue
        else:
            break

    avg_score = float((math_score + physics_score + chemistry_score) / 3)

    rank = check_rank(avg_score)

    student["math_score"] = math_score
    student["physics_score"] = physics_score
    student["chemistry_score"] = chemistry_score
    student["avg_score"] = avg_score
    student["rank"] = rank
    print("Đã cập nhật điểm của sinh viên thành công")


def delete_student(list):
    while True:
        delete_student_id = input("Nhập mã sinh viên cần xoá: ").strip().upper()
        if delete_student_id == "":
            print("Lỗi! Mã sinh viên không được để trống")
            continue
        found = False
        for student in list:
            if student["student_id"] == delete_student_id:
                found = True
                print("=" * 90)
                print(
                    "{student_id:<12} | {student_name:<13} | {math_score:<9} | {physics_score:<7} | {chemistry_score:<8} | {avg_score:<15} | {rank}".format_map(
                        student
                    )
                )
                print("=" * 90)
                while True:
                    comfirm = (
                        input(
                            f"Bạn có xác nhận xóa sinh viên {delete_student_id} (yes/no): "
                        )
                        .strip()
                        .lower()
                    )
                    if comfirm == "yes":
                        list.remove(student)
                        print(f"Đã xoá thành công sinh viên {student['student_id']}")
                    elif comfirm == "no":
                        print("Đã hủy bỏ thao tác")
                        break
                    else:
                        print("Lựa chọn không hợp lệ!")
                        continue
        if not found:
            print("không tìm thấy sinh viên này")
        else:
            break


def statistical_rank(list):
    count_good = 0
    count_rather = 0
    count_medium = 0
    count_weak = 0
    for student in list:
        if student["rank"] == "Giỏi":
            count_good += 1
        elif student["rank"] == "Khá":
            count_rather += 1
        elif student["rank"] == "Trung Bình":
            count_medium += 1
        else:
            count_weak += 1
    print(f"Số sinh viên xếp hạng giỏi là: {count_good}")
    print(f"Số sinh viên xếp hạng khá là: {count_rather}")
    print(f"Số sinh viên xếp hạng trung bình là: {count_medium}")
    print(f"Số sinh viên xếp hạng yếu là: {count_weak}")


def search_student(list):
    keyword = input("Nhập mã sinh viên hoặc tên cần tìm: ").strip().upper()
    found = False
    print("============= Thông tin sinh viên =============")
    print("=" * 90)
    for student in list:
        if student["student_id"] == keyword:
            found = True
        elif keyword in student["student_name"].upper():
            found = True
        print(
            "{student_id:<12} | {student_name:<13} | {math_score:<9} | {physics_score:<7} | {chemistry_score:<8} | {avg_score:<15} | {rank}".format_map(
                student
            )
        )
    print("=" * 90)
    if not found:
        print("Không tìm thấy sinh viên")


def main():
    while True:
        print("""
=============== Hệ Thống Quản Lý Sinh Viên ===============
        1. Hiển thị danh sách sinh viên
        2. Tiếp nhận sinh viên (Thêm sinh viên)
        3. Cập nhật kết quả học tập (Cập nhật điểm)
        4. Xoá sinh viên
        5. Tìm kiếm sinh viên
        6. Thống kê điểm TB
        7. Thoát 
==========================================================
""")
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                display_students(students_list)
            case "2":
                add_student(students_list)
            case "3":
                update_student_score(students_list)
            case "4":
                delete_student(students_list)
            case "5":
                search_student(students_list)
            case "6":
                statistical_rank(students_list)
            case "7":
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ!")


main()
