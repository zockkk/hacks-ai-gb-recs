const API_HOST = "http://localhost:8000"
export const baseApiService = {
  get: async (url: string) => {
    const response = await fetch(`${API_HOST}${url}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    return await response.json();
  },
  post: async (url: string, data: any) => {
    const response = await fetch(`${API_HOST}${url}`, {
      method: "POST",
      body: data instanceof FormData ? data : JSON.stringify(data),
    });
    return await response.json();
  },
}