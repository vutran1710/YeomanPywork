from fastapi import APIRouter

router = APIRouter()


@router.post("/login/use-token")
def get_products():
    """
    Test access token
    """
    return {
        "product": ["iphone", "apple watch", "macbook"]
    }
