# 프로젝트 설정

이 프로젝트는 **Poetry**를 사용하여 의존성 관리를 수행합니다. Poetry는 Python 패키지 관리를 쉽게 하고, 가상 환경을 통합적으로 관리할 수 있게 해줍니다.

## 1. Poetry 설치

Poetry를 설치하려면 다음 명령어를 실행하세요:

```bash
curl -sSL https://install.python-poetry.org | python3 -
# or
pip install poerty
```

설치가 완료되면, Poetry 명령어가 정상적으로 동작하는지 확인합니다:

```bash
poetry --version
```

## 2. Poetry를 이용한 프로젝트 설정

### 2-1. 프로젝트 생성

다음 명령어로 새로운 Poetry 프로젝트를 생성할 수 있습니다:

```bash
poetry new your_project_name
```

또는, 기존 프로젝트에서 Poetry를 초기화하려면 프로젝트 루트에서 다음 명령어를 실행합니다:

```bash
poetry init
```

Poetry가 상호작용형 방식으로 `pyproject.toml` 파일을 생성하도록 안내합니다.

### 2-2. 의존성 설치

프로덕션 및 개발 환경에서 사용할 패키지를 설치하려면 다음 명령어를 사용합니다:

#### 프로덕션 패키지 설치

```bash
poetry add package_name
```

#### 기타 의존성 패키지 설치

```bash
poetry add --dev package_name  # 개발
poetry add --group test package_name  # 테스트
```

### 2-3. 가상 환경 활성화 및 관리

Poetry는 가상 환경을 자동으로 관리합니다. 다음 명령어로 가상 환경을 활성화할 수 있습니다:

```bash
poetry shell
```

가상 환경을 비활성화하려면 `exit` 명령어를 사용합니다.

### 2-4. 의존성 설치 및 업데이트

`pyproject.toml` 파일에 정의된 모든 의존성을 설치하려면 다음 명령어를 실행하세요:

```bash
poetry install  # install all
poetry install --with test
poetry install --with dev test
poetry install --without dev test eda
```

의존성을 업데이트하려면 다음 명령어를 실행합니다:

```bash
poetry update
```

### 2-5. 테스트 실행

테스트를 실행하기 위해서는 개발 의존성에 `pytest`를 추가한 뒤, 다음과 같이 테스트를 실행할 수 있습니다:

```bash
poetry run pytest
```

### 2-6. 프로젝트 빌드

프로젝트를 패키징하려면 다음 명령어를 사용하여 빌드할 수 있습니다:

```bash
poetry build
```

이 명령어는 프로젝트를 배포 가능한 `.tar.gz` 또는 `.whl` 파일로 패키징합니다.
