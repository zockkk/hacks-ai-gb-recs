import {baseApiService} from "@/services/api/base.api.service";

export const dataProcessApiService = {
  process: async (data: any) => {
    return baseApiService.post(`/process_data`, data)
  },
  upload: async (data: FormData) => {
    return baseApiService.post(`/upload_file`, data)
  }
} as const