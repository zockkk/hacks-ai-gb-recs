'use client'
import {TextArea} from "@/components/TextArea/TextArea";
import {FormEvent, useCallback, useState} from "react";
import {FileUploader} from "@/components/FileUploader/FileUploader";
import {Button} from "@/components/Button/Button";
import {dataProcessApiService} from "@/services/api/data_process.api.service";
interface ResultItem {
  cosine_dist_description: number
  cosine_dist_title: number
  text: string
  title: string
}
export function Form() {
  const [result, setResult] = useState<ResultItem[]>([]) // [1
  const handleSubmit = useCallback(async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const response = await dataProcessApiService.process({ text: e.currentTarget.message.value })
    setResult(response.recs)
  }, [])

  const handleFileUpload = useCallback(async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);

    const response: { recs: ResultItem[] } = await dataProcessApiService.upload(formData);
    setResult(response.recs)
  }, [])

  return (
    <div>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <div className="flex">
          <TextArea/>
        </div>

        <div className="flex items-center justify-end space-x-4">
          <Button type="submit">Отправить</Button>
          <FileUploader onChange={handleFileUpload}/>
        </div>
      </form>

      {result.length > 0 && result.map((item, index) => (
        <div key={index} className="border p-4 rounded shadow">
          <div>{item.title}</div>
          <div className="flex justify-between">
            <span>Косинусное расстояние по заголовку: {item.cosine_dist_title}</span>
            <span>Косинусное расстояние по описанию: {item.cosine_dist_description}</span>
          </div>
      </div>
      ))}
    </div>
  )
}