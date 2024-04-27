'use client'
import {ChangeEvent, useCallback, useRef, useState} from "react";
import {Button} from "@/components/Button/Button";

interface Props {
  onChange: (file: File) => void;
}

export function FileUploader(props: Props) {
  const { onChange } = props;
  const [isLoading, setIsLoading] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null);

  const onButtonClick = useCallback(() => {
    fileInputRef.current!.click();
  }, []);

  const handleChange = useCallback(async (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    console.log('UploaderFile', file?.name)
    if (!file) return;

    onChange(file);
  }, [onChange]);

  return (
    <div className="overflow-hidden relative flex">
      <Button
        onClick={onButtonClick}
      >
        Загрузить PDF файл
      </Button>
      <input
        ref={fileInputRef}
        onChange={handleChange}
        className="hidden"
        type="file"
        accept=".pdf"
      />
    </div>
  )
}