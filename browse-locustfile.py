from locust import task, run_single_user
from locust import FastHttpUser


class BrowseUser(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    @task
    def browse(self):
        response = self.client.get(
            "/browse",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        )
        # Validate response
        if response.status_code == 200 and "<html>" in response.text:
            response.success()
        else:
            response.failure(f"Unexpected response: {response.status_code}")

if __name__ == "__main__":
    run_single_user(BrowseUser)
