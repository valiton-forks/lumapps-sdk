from _pytest.outcomes import Skipped
import httpx
import pytest
import jwt 
import base64
import json
import datetime 
import calendar

from lumapps.api.errors import (
    LumAppsJwtTokenExpiredError,
    LumAppsJwtInvalidClaimError,
    LumAppsJwtCustomError,
    LumAppsJwtHeaderError
)

from lumapps.api.lumapps_jwt import LumappsJWT


TOKEN = b"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6InN5bi1rZXktdjAifQ.eyJpc3MiOiJodHRwczovL2xvZ2luLmx1bWFwcHMuY29tL3YxIiwiaWF0IjoxNjIxODYwMzMwLCJleHAiOjE2MjE4NjM5MzAsImF1ZCI6Imh0dHBzOi8vbHVtc2l0ZXMuYXBwc3BvdC5jb20vX2FoL2FwaS9sdW1zaXRlcyIsInN1YiI6IjY3NTM1NTI3ODM3Njk2MDAiLCJvcmdhbml6YXRpb25JZCI6IjU3Njk5Mjg4NTg2NjQ5NjAiLCJlbWFpbCI6ImFpQGx1bWFwcHMuY29tIn0.XOgTJNt5h0eG65UYxRLNMfpcvGE-TBxftNATjfHoL8JoNovB_McP96kgvka2FZN6u89RcrT3enHqOUS-vMpeRvmzjJ6UruUDJaHB4km2blK2nO6zZvpnmbFnQBLj856vendqbesni_a2CHLATbc44aHs6fdEHMREjBsbmTr1QU6KD6IBBtMPsqvvwI3I7ggS4FeReRlmCV5rd8ZgwE0Nft1_3aoLuqUUtNw9cdxm87swG-ezPQugt2XVfpPo-t4NLjZiRpnSfu1Oqd9jlQWEFKiIUPJnTslKNIzE9pXMaJDTXfu26aSLttEm_qiJB9rhqRevBxEm-Zj5AVQ6OmlrLUSCV0hpokZpKYkAaOgwjnxggbujxy9jn2ItaNblb_sL0mz-S7VM3CEbpAwCqIhAVWOQXpReAyjECKfmjU5jRdjtIEXy0rEhdI0R8UwTYWbukGZyLplI434GDZAf-MvqjhxZdCTGinESCPJJeDvDhI_hSEn7QY08QdGdoLGIl4wQKu3JPKQQ2d8zSruQvLETFJReWrCyooJMMm6Rr0tTxVPL4I7nqsYlYAMBY3KkhDALtQF4kTcq1tpHupojv7hxzOGZpBNSlNLhuqwtXQwUkXo96anTITA6h2An_S2nRckaKpTWUoGtJxLxjjLoLuFJjzW8XJqOYtbW_fH0HX7qCg4"

def test_decode_valid():
    with pytest.raises(LumAppsJwtTokenExpiredError) as exinfo:
        payload = LumappsJWT().decode(TOKEN)
        assert str(exinfo.value) == "Token is expired."
        assert payload["aud"] == "https://lumsites.appspot.com/_ah/api/lumsites"
        assert payload["email"] == "ai@lumapps.com"
