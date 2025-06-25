import os
import tarfile
import shutil


def ensure_dir(path):
    """디렉토리가 존재하지 않으면 생성"""
    os.makedirs(path, exist_ok=True)


def compress_to_tar(src_dir, out_path):
    """디렉토리 전체를 tar.gz로 압축"""
    with tarfile.open(out_path, "w:gz") as tar:
        tar.add(src_dir, arcname='.')
    return out_path


def extract_tar(tar_path, extract_to):
    """tar.gz 파일을 지정한 위치에 압축 해제"""
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=extract_to)


def clear_dir(path):
    """디렉토리 내용을 비움 (재사용 가능하게 초기화)"""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def file_exists(path):
    """파일 존재 여부 확인"""
    return os.path.isfile(path)


def read_text_file(path):
    """텍스트 파일 읽기"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_text_file(path, content):
    """텍스트 파일 쓰기"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
